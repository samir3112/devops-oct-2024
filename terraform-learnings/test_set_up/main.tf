// "provider" is a plugin which allow terraform to 
// interact with other services like cloud providers
// following snippet describes aws plugin

provider "aws"{
    region="us-east-1"
//  install aws cli, run aws configure and no need to following    
//  access_key = "XXXXXXXXXXXXX"
//  secret_key = "XXXXXXXXXXXXXXXXXXXXXXXXXX"
}

// "resource" is a fundamental building block within a Terraform configuration that represents 
// a specific piece of infrastructure, like a virtual machine, vpc
// Terraform manages resource creation, modification, and deletion 
// It describe infrastructure as a code

resource "aws_vpc" "vpcbytf"{
    cidr_block = "10.1.0.0/16"
    tags = {
      Terraform = "true"
      Name = "VPC By TF"
    }
}
