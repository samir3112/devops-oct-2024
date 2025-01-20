// these outputs, will be input to main.tf

output "vpc_id" {
  value = aws_vpc.vpc-by-tf.id
}

output "public_subnet_id" {
  value = aws_subnet.public-subnet-by-tf.id
}
