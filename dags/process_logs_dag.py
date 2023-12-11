from airflow.decorators import dag, task
from pendulum import datetime
from airflow.providers.microsoft.azure.operators.adx import AzureDataExplorerQueryOperator
from airflow.providers.microsoft.azure.operators.cosmos import AzureCosmosInsertDocumentOperator
from azure.identity import ClientSecretCredential
from azure.storage.queue import QueueClient
from airflow.models import Variable
import json
import uuid
import os
import logging

logger = logging.getLogger(__name__)

@dag(
    schedule="@hourly",
    start_date=datetime(2023, 12, 7, 20, 0, 0),
    catchup=False,
    default_args={
        "retries": 2
    }
)
def process_logs_dag():

    @task()
    def query_kusto():       
        queryResult =  AzureDataExplorerQueryOperator(
            task_id='logs',
            query='''
                let 4xx = apiLogs
                | where message startswith "4XX Error Random number"
                | where startofday(['datetime']) == startofday(now())
                | where datetime_part("hour", ['datetime']) == datetime_part("hour", now())
                | extend type = "4XX"
                | project correlationId, type;
                let 5xx = apiLogs
                | where message startswith "InternalServer Error Random number"
                | where startofday(['datetime']) == startofday(now())
                | where datetime_part("hour", ['datetime']) == datetime_part("hour", now())
                | extend type = "5XX"
                | project correlationId, type;
                apiLogs
                | where message endswith "returned successfully"
                | where startofday(['datetime']) == startofday(now())
                | where datetime_part("hour", ['datetime']) == datetime_part("hour", now())
                | extend type = "2XX"
                | project correlationId, type
                | union ( ['4xx'] )
                | union ( ['5xx'] )
            ''',
            database=Variable.get("DEMO_KUSTO_DATABASE"),
            azure_data_explorer_conn_id='adx'
        ).execute(context=None)
        return json.loads(queryResult)["data"]

    @task()
    def process_kusto_data(kusto_data):
        return {
            "id": str(uuid.uuid4()),
            "2XX": len(list(filter(lambda x: x["type"] == "2XX", kusto_data))),
            "4XX": len(list(filter(lambda x: x["type"] == "4XX", kusto_data))),
            "5XX": len(list(filter(lambda x: x["type"] == "5XX", kusto_data))),
            "total": len(kusto_data),
            "5XX_correlationIds": list(map(lambda x: x["correlationId"], filter(lambda x: x["type"] == "5XX", kusto_data))),
        }

    @task()
    def store_summarized_data(process_kusto_data):
        AzureCosmosInsertDocumentOperator(
            task_id='store_summarized_data',
            database_name=Variable.get("DEMO_COSMOS_DATABASE"),
            collection_name=Variable.get("DEMO_COSMOS_COLLECTION"),
            document=process_kusto_data,
            azure_cosmos_conn_id='cosmos_db'
        ).execute(context=None)

    @task()
    def send_alert_to_queue(process_kusto_data):
        queue_client = QueueClient(
            account_url=Variable.get("DEMO_STORAGE_ACCOUNT"), 
            queue_name=Variable.get("DEMO_QUEUE_NAME"),
            credential=ClientSecretCredential(
                Variable.get('DEMO_TENANT_ID'),
                Variable.get('DEMO_CLIENT_ID'),
                Variable.get('DEMO_CLIENT_SECRET')))
        queue_client.send_message(json.dumps(process_kusto_data))

    kusto_data = query_kusto()
    processed_data = process_kusto_data(kusto_data)
    store_summarized_data(processed_data)
    send_alert_to_queue(processed_data)


process_logs_dag()
