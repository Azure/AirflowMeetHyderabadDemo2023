from airflow.models import Variable
from azure.identity import ClientSecretCredential


def build_clientSecretCredential():
    return ClientSecretCredential(
        tenant_id=Variable.get("DEMO_TENANT_ID"),
        client_id=Variable.get("DEMO_CLIENT_ID"),
        client_secret=Variable.get("DEMO_CLIENT_SECRET"),
    )