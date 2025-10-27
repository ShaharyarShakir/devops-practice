resource "aws_s3_bucket" "remote_s3" {
  bucket = "my-tf-backend-bucket-form"

  tags = {
    Name = "my-tf-backend-bucket-form"
  }
}
