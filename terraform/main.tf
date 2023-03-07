# Configure the Azure provider
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0.2"
    }
  }

  required_version = ">= 1.1.0"
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "okta-sample-test-rg"
  location = "East US"
  tags = {
    environment = "test"
  }
}

resource "azurerm_app_service_plan" "example" {
  name                = "okta-sample-test-asp"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_app_service" "example" {
  name                = "okta-sample-test"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id

  site_config {
    #linux_fx_version = "PYTHON|3.10"
  }

  app_settings = {
    "WEBSITE_WEBDEPLOY_USE_SCM" = "false"
    "SCM_TYPE" = "None"
  }
}