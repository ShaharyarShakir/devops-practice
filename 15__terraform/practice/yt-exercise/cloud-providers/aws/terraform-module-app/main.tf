
module "dev-infra" {
  source         = "./intra-app"
  env            = "dev"
  bucket_name    = "infra-app-bucket"
  instance_count = 1
  instance_type  = "t2.micro"
  ec2_ami        = "ami-0de716d6197524dd9"
  hash_key       = "LockedID"
}
module "prod-infra" {
  source         = "./intra-app"
  env            = "prod"
  bucket_name    = "infra-app-bucket"
  instance_count = 1
  instance_type  = "t2.medium"
  ec2_ami        = "ami-0de716d6197524dd9"
  hash_key       = "LockedID"
}
module "stage-infra" {
  source         = "./intra-app"
  env            = "stage"
  bucket_name    = "infra-app-bucket"
  instance_count = 1
  instance_type  = "t2.small"
  ec2_ami        = "ami-0de716d6197524dd9"
  hash_key       = "LockedID"
}
