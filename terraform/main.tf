terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  required_version = ">= 1.5.0"
}

provider "aws" {
  region = "us-east-1"
}

# Create an ECR repository to hold our container images
resource "aws_ecr_repository" "github_app_repo" {
  name                 = "github-app-repo"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Environment = "Dev"
    Project     = "Python-Zero-To-Hero"
    ManagedBy   = "Terraform"
  }
}

# Export the ECR Repository URL upon successful deployment
output "ecr_repository_url" {
  value       = aws_ecr_repository.github_app_repo.repository_url
  description = "The URI of the created AWS ECR Repository"
}
