provider "aws" {
  region = "us-east-1"
  //  install aws cli, run aws configure and no need to following    
  //  access_key = "XXXXXXXXXXXXX"
  //  secret_key = "XXXXXXXXXXXXXXXXXXXXXXXXXX"
}



resource "aws_vpc" "vpc-by-tf" {
  cidr_block = var.vpc_cidr
  tags = {
    Terraform = "true"
    Name      = "VPC By TF"
  }
}
