# key pair creation
resource "aws_key_pair" "developer" {
  key_name   = "${var.env}-infra-key-ec2"
  public_key = file("terra-key-ec2.pub")
  tags = {
    "Environement" = var.env
  }
}
# VPC creation
resource "aws_default_vpc" "default" {
  tags = {
    Name = "Default VPC"
  }
}
# Security group creation
resource "aws_security_group" "terra_sg" {
  name        = "${var.env}-infra-sg"
  description = "Security group for EC2 instances using Terraform"
  vpc_id      = aws_default_vpc.default.id # interpolation ==> way to reference other resources in Terraform block
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    "Name" = "${var.env}-terra-instance-sg"
  }
}

# EC2 instance creation
resource "aws_instance" "my_terra" {
   count = var.instance_count
  depends_on      = [aws_security_group.terra_sg, aws_key_pair.developer]
  key_name        = aws_key_pair.developer.key_name
  security_groups = [aws_security_group.terra_sg.name]
  ami             = var.ec2_ami
  instance_type   = var.instance_type
  root_block_device {
    volume_size = var.env == "prod" ? 12 : 15
    volume_type = "gp3"
  }
  tags = {
    Name = "${var.env}-infra-instance-${count.index + 1}"
    Environment = var.env
  }
}
