resource "aws_vpc" "vpc-by-tf" {
  cidr_block = var.vpc_cidr
  tags = {
    Terraform = "true"
    Name      = "VPC By TF"
  }
}

data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_subnet" "public-subnet-by-tf" {
  vpc_id                  = aws_vpc.vpc-by-tf.id
  cidr_block              = var.public_subnet_cidr
  availability_zone       = data.aws_availability_zones.available.names[0]
  map_public_ip_on_launch = true

  tags = {
    Name = "Public Subnet by TF"
  }
}
