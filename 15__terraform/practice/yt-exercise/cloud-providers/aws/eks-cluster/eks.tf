module "eks" {
source = "terraform-aws-modules/eks/aws"
version = "~> 21.0"

  name               = local.name
  kubernetes_version = "1.33"
    endpoint_public_access = true

  vpc_id                   = module.vpc.default_vpc_id
  subnet_ids               = module.vpc.private_subnets
  control_plane_subnet_ids = module.vpc.intra_subnets

  eks_managed_node_groups = {

    terra-eks-ng = {
# cluster addons
  cluster_addons = {
    vpc-cni = {
      most_recent = true
    }
    kube-proxy = {
      most_recent = true
    }
    coredns = {
      most_recent = true
    }
  }
    name = local.name
    instance_type = "t3.medium"
    attach_cluster_primary_security_group = true
      min_size     = 2
      max_size     = 4
      desired_size = 2
      capacity_type = "SPOT"
  }
  }
  tags = {
    Environment = local.env
    Terraform = "true"
  }

}
