// these output, will be input to main.tf, where intrenet-gateway-module is called
output "vpc-public_subnet_id" {
  value = module.vpc.public_subnet_id
}

output "vpc-security_group_id" {
  value = module.vpc.security_group_id
}
