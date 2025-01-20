provider "aws" {
  region = "us-east-1"
}

// module is a collection of configuration files in a directory 
// that groups resources for a specific task like vpc, gateway

// call VPC module
// pass value of env var
module "vpc" {
  source = "./vpc-module"
  env    = var.env
}

// create ec2 instance
resource "aws_instance" "ec2-by-tf" {
  ami           = "ami-0a3c3a20c09d6f377"
  instance_type = "t2.micro"
  subnet_id     = module.vpc.public_subnet_id // output of vpc module
  tags = {
    Terraform   = "true"
    Name        = "EC2 By TF"
    Environment = var.env
  }
}


// will output following after terraform apply
output "public_ip_address" {
  value = aws_instance.ec2-by-tf.public_ip
}

output "private_ip_address" {
  value = aws_instance.ec2-by-tf.private_ip
}
