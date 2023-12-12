## Overview
 
Contoso Corporation faces challenges in efficiently analyzing API failures recorded in Kusto logs, hindering prompt issue identification. This GitHub repository offers a robust solution for analyzing API failures recorded in Kusto using Astronomer on Azure. The workflow seamlessly configures an Astronomer resource from the Azure, establishes Single Sign-On (SSO) integration with an Astronomer organization in a designated workspace, and deploys a Directed Acyclic Graph (DAG) through the user-friendly Astronomer or Airflow UI. Solution implemented is described in the image follows:
<img width="1489" alt="Worksflow" src="https://github.com/Azure/AirflowMeetHyderabadDemo2023/assets/40313233/85717726-9890-4f60-b456-597a782cdbf8">

## Pre-requisite
1. **App Registration in Azure Entra**: Create and register your Azure AAD/Entra application and keep ApplicationId, ClientSecret, TenantId with you for later configurations and settings, know more about Apps on Azure Entra [here](https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals?tabs=browser).
   
![image](https://github.com/Azure/AirflowMeetHyderabadDemo2023/assets/40313233/1c5a5eda-65c0-442d-b612-89ff4d91181b)
![image](https://github.com/Azure/AirflowMeetHyderabadDemo2023/assets/40313233/9cffe25f-d6f8-4f34-a93a-f1204658ac8c)
![image](https://github.com/Azure/AirflowMeetHyderabadDemo2023/assets/40313233/021f6659-a4bd-433b-a335-69727ea2f5e1)

2. **Assign App to Kusto Database**: Assign application to kusto database and keep Data Explorer Connection String, ClientId, ClientSecret and TenantID for the app for further steps. Make sure necessary data is present in Kusto Database. To learn more about Kusto and Azure Data Explorer refer [link](https://learn.microsoft.com/en-us/azure/data-explorer/data-explorer-overview)
   
![image](https://github.com/Azure/AirflowMeetHyderabadDemo2023/assets/40313233/113edfa5-5a25-4e0d-8aa9-ba98f31a1ecf)
![image](https://github.com/Azure/AirflowMeetHyderabadDemo2023/assets/40313233/76fb5f04-8dc6-412f-b2c6-06d169f45238)

3. **Create CosmosDB**: Create Cosmos DB and keep secret and connection string safe. To learn more about CosmoDB refer [link](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction)
   
![image](https://github.com/Azure/AirflowMeetHyderabadDemo2023/assets/40313233/40b79409-0a26-4e74-9142-cb8b6585b732)
![image](https://github.com/Azure/AirflowMeetHyderabadDemo2023/assets/40313233/2aaba837-6a70-47f3-a3c7-558ac8e769c7)

4. **Create StorageAccount**: Create Storage Account, and queue and provide necessary permissions for them to app created in first step. To learn more about storage queue refer [link](https://learn.microsoft.com/en-us/azure/storage/queues/storage-queues-introduction)
![image](https://github.com/Azure/AirflowMeetHyderabadDemo2023/assets/40313233/8e246663-75a0-4bdf-8fe3-6a8bca712911)



## How to run?
1. Go to [Azure portal](https://portal.azure.com) and search for Astronomer and hit Create. ![image](https://github.com/Azure/AirflowMeetHyderabadDemo2023/assets/40313233/675dfa24-a4b9-417b-b2b5-620a743f975d)
2. Fill the resource creation form with details including Subscription, Resource Group, Azure Resource Name, Region, Astro Organization Name, Astro Workspace Name, Billing Term, Price+Payment options and hit "review+create". ![image](https://github.com/Azure/AirflowMeetHyderabadDemo2023/assets/40313233/8b6c0e3c-d99e-4c2a-b11a-4aa77a3b00e3)
3.  Once Create is succeful open the create resource and navigate to Astronomer from using the SSO link in resoure. ![image](https://github.com/Azure/AirflowMeetHyderabadDemo2023/assets/40313233/6ce96b74-af2e-4b90-b777-faad6ca0bd44)
4.  Create a new deployment on Astronomer portal and hit "Create Deployment". ![image](https://github.com/Azure/AirflowMeetHyderabadDemo2023/assets/40313233/69fcc823-142a-40f1-aff5-d06ef5ddba94)
5.  Clone this repository use: `git clone https://github.com/Azure/AirflowMeetHyderabadDemo2023`
6.  Install Astro CLI, use: <a href="https://docs.astronomer.io/astro/cli/install-cli">https://docs.astronomer.io/astro/cli/install-cli</a>
7.  Use `astro login` and follow prompted steps to login using the same your microsoft account used in Azure.
8.  Use `astro workspace list` to list your workspaces and make sure that you are in the currect workspace.
9.  Use `astro deploy` to deploy the code in your astro deployment created in step 4.
10.  From deployment created in step 4, navigate to "Open in Airflow" ![image](https://github.com/Azure/AirflowMeetHyderabadDemo2023/assets/40313233/feb860ed-5cad-480f-9461-73c3ecbd24c4)
11.  In Airflow UI, select Admin > Variables and create following variables
     
| **Varaible**             | **Value**                                             |
|--------------------------|-------------------------------------------------------|
| `DEMO_CLIENT_ID`         | ClientId/AppId for AAD/Entra Application Created      |
| `DEMO_CLIENT_SECRET`     | ClientSecret for the above app                        |
| `DEMO_COSMOS_COLLECTION` | Collection Name to be used in CosmosDB                |
| `DEMO_COSMOS_DATABASE`   | Database Name to be used in CosmosDB                  |
| `DEMO_KUSTO_DATABASE`    | Database Name to be used in Kusto/Azure Data Explorer |
| `DEMO_QUEUE_NAME`        | Name of the queue to be used                          |
| `DEMO_STORAGE_ACCOUNT`   | Storage account name to be used                       |
| `DEMO_TENANT_ID`         | TenantId for components to used.                      |
12.  Create a new connection with `adx` id for Azure Data Explorer from Admin > Connections. Select Connection Type as: `Azure Data Explorer`, provide cluster url, provide client/appId in cluster name, provide clientSecret in Password, add TenatID and in Authentication Method select `AAD_APP`. Ref screenshot below: ![image](https://github.com/Azure/AirflowMeetHyderabadDemo2023/assets/40313233/e1f31116-7ea9-482c-b424-5f5399b71bee)
13.  Create another connection with id as `cosmos_db` and select connection type as: `Azure CosmosDB`, provide CosmosEndpoint and in Cosmos Master Key Token provide primary key for Comsos DB  ![image](https://github.com/Azure/AirflowMeetHyderabadDemo2023/assets/40313233/764ce919-1586-4c84-8864-18c45b5eda8b)
14.  Once done, go ahead and click run from Astronomer portal, your DAG should be running in a few minutes. 


## DAG Details
The DAG orchestrates the following tasks:
 
1. Log Retrieval
 
    Fetch API failure logs from Kusto for analysis.
 
2. Data Analysis
 
    Analyze the retrieved logs to identify patterns and trends related to API failures.
 
3. Azure Cosmos DB Storage
 
    Store the processed data in Azure Cosmos DB for future reference and analysis.
 
4. Alert Generation and Azure Queue Storage
 
    Trigger alerts based on predefined criteria for proactive issue identification and forward generated alerts to Azure Queue Storage for further processing and action.
 
## Contributing
 
This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.
 
When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.
 
This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
 
## Trademarks
 
This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
