variable "ec2_instance_type" {
  description = "Type of EC2 instance to create"
  type        = string
  default     = "t2.micro"
}
variable "ec2_default_root_storage_size" {
  description = "Size of the root block device in GB"
  type        = number
  default     = 8
}
variable "ec2_ami" {
  description = "AMI ID for the EC2 instance"
  type        = string
  default     = "ami-0de716d6197524dd9"
}
variable "ec2_storage_type" {
  description = "Type of storage for the EC2 instance"
  type        = string
  default     = "gp3"
}
variable "env" {
  description = "Environment type (e.g., dev, prod)"
  type        = string
  default     = "prod"

}
