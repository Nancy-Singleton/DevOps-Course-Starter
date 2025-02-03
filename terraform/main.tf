terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.8"
    }
  }

  backend "azurerm" {
    resource_group_name  = "cohort32-33_NanSin_ProjectExercise"
    storage_account_name = "nansinstorageaccount01"
    container_name       = "nansin-container-01"
    key                  = "terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
  subscription_id = "d33b95c7-af3c-4247-9661-aa96d47fccc0"
}

data "azurerm_resource_group" "main" {
  name = "cohort32-33_NanSin_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
  name                = "${var.prefix}-nansin-service-plan-01"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_web_app" "main" {
  name                = "${var.prefix}-nansin-todo-app-01"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id

  site_config {
    application_stack {
      docker_image_name   = "nancysingleton036/todo-app:prod"
      docker_registry_url = "https://index.docker.io"
    }
  }

  app_settings = {
    "FLASK_APP"             = "todo_app/app"
    "FLASK_DEBUG"           = false
    "SECRET_KEY"            = "secret-key"
    "CONNECTION_STRING"     = azurerm_cosmosdb_account.db_account.primary_mongodb_connection_string
    "DATABASE_NAME"         = azurerm_cosmosdb_mongo_database.db.name
    "ITEMS_COLLECTION_NAME" = "to_do_items"
    "LOGGLY_TOKEN"          = "${var.loggly_token}"
  }
}

resource "azurerm_cosmosdb_account" "db_account" {
  name                 = "${var.prefix}-nansin-dbaccount-01"
  location             = data.azurerm_resource_group.main.location
  resource_group_name  = data.azurerm_resource_group.main.name
  offer_type           = "Standard"
  kind                 = "MongoDB"
  mongo_server_version = "7.0"

  capabilities {
    name = "EnableMongo"
  }

  consistency_policy {
    consistency_level = "Eventual"
  }

  geo_location {
    location          = "uksouth"
    failover_priority = 0
  }

  capabilities {
    name = "EnableServerless"
  }
}

resource "azurerm_cosmosdb_mongo_database" "db" {
  name                = "${var.prefix}-nansin-db-01"
  resource_group_name = azurerm_cosmosdb_account.db_account.resource_group_name
  account_name        = azurerm_cosmosdb_account.db_account.name

  lifecycle {
    prevent_destroy = true
  }
}
