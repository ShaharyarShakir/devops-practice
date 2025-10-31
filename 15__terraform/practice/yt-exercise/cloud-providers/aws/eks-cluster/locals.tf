locals{
 name = "terra-eks-cluster"
region = "us-east-1"
vpc_cidr = "10.0.0.0/16"
azs = ["us-east-1a", "us-east-1b"]
private_subnets = ["10.0.1.0/24","10.0.2.0/24"]
public_subnets = ["10.0.4.0/24","10.0.5.0/24"]
intra_subnets = ["10.0.7.0/24","10.0.8.0/24"]
env = "dev"
}
