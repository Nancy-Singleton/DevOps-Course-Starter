# Set Up `.env` File

- Clone a new `.env` file from the `.env.template` to store local configuration options:

```bash
$ cd env && cp .env.template .env
```

# Mongo DB

The project requires a MongoDB database.

Before running the app locally, you will need to add a connection string to your local `env` file.

You can create a new Cosmos DB database in Azure via the following commands:
- Create a CosmosDB Account: `az cosmosdb create --name <cosmos_account_name> --resource-group <resource_group_name> --kind MongoDB --capabilities EnableServerless --server-version 4.2`
- Create `new` MongoDB database under that account `az cosmosdb mongodb database create --account-name <cosmos_account_name> --name <database_name> --resource-group <resource_group_name>`

Given an existing Cosmos DB database, you can find the connection string in the Azure portal under Settings > Connection Strings.