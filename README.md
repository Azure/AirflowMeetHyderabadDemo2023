# Overview
 
Contoso Corporation faces challenges in efficiently analyzing API failures recorded in Kusto logs, hindering prompt issue identification. This GitHub repository offers a robust solution for analyzing API failures recorded in Kusto using Astro on Azure. The workflow seamlessly configures an Astronomer resource from the Azure Marketplace, establishes Single Sign-On (SSO) integration with an Astronomer organization in a designated workspace, and deploys a Directed Acyclic Graph (DAG) through the user-friendly Astronomer or Ai
 
## Key Steps
1. Astronomer Resource Creation
 
    Begin by creating an Astronomer resource from the Azure Marketplace. This resource will be seamlessly linked via Single Sign-On (SSO) with an Astronomer organization within the designated workspace.
 
2. Deployment through Astronomer or Airflow UI
 
    Create a deployment on the above mentioned Astronomer organization ad utilize the Astronomer or Airflow UI to deploy a DAG specifically designed for retrieving and analyzing logs from Kusto. The processed data will be stored in Azure Cosmos DB.
 
3. Alert Triggering and Azure Queue Storage
 
    The DAG is configured to parallelly trigger alerts based on the processed data. These alerts are then forwarded to Azure Queue Storage for subsequent processing.
 
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