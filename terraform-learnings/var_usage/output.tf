output "vpc_id" {
  value = aws_vpc.vpc-by-tf.id
}

output "cidr_range" {
  value = aws_vpc.vpc-by-tf.cidr_block
}
