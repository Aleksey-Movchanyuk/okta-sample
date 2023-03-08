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
  kind     = "linux"
  reserved = true
}

resource "azurerm_app_service" "example" {
  name                = "okta-sample-test"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id

  site_config {
    always_on        = true
    linux_fx_version = "PYTHON|3.9"
    #app_command_line = "gunicorn --bind=0.0.0.0 --timeout 600 api:app"
  }

  app_settings = {
    "SCM_DO_BUILD_DURING_DEPLOYMENT" = true
  }
}

resource "null_resource" "deploy_zip" {
  depends_on = [azurerm_app_service.example]
  provisioner "local-exec" {
    command = "az webapp deployment source config-zip -g ${azurerm_resource_group.example.name} -n ${azurerm_app_service.example.name} --src ${var.zip_file}"
  }
}


# Set variables
variable "zip_file" {
  default = "../okta-sample-backend/dist/okta-sample-backend-1.0.zip"
}