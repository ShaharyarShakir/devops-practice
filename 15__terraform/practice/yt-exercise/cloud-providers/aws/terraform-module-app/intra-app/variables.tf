variable "env" {
  description = "This is environment variable for my infrastructure"
  type = string
}
variable "bucket_name" {
  description = "Name of the S3 bucket"
  type = string
}
variable "instance_count" {
  description = "Number of EC2 instances to create"
  type        = number

}
variable "instance_type" {
  description = "Type of EC2 instance to create"
  type        = string

}
variable "ec2_ami" {
  description = "AMI ID for the EC2 instances"
  type        = string

}
variable "hash_key" {
  description = "Hash key for the DynamoDB table"
  type        = string
}
