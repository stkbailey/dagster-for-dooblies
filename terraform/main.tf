terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0.0"
    }
  }
  cloud {
    organization = "stkbailey"
    workspaces {
      name = "dagster-for-dooblies"

    }
  }
}

provider "aws" {
  region                  = var.region
  shared_credentials_file = var.shared_credentials_file
  profile                 = var.profile_name
}

locals {
  cluster_name   = "dagster"
}

module "ecs" {
  source = "terraform-aws-modules/ecs/aws"
  name = local.cluster_name
  container_insights = true
  capacity_providers = ["FARGATE", "FARGATE_SPOT"]

  default_capacity_provider_strategy = [
    {
      capacity_provider = "FARGATE_SPOT"
    }
  ]

  tags = {
    Environment = "Development"
  }
}