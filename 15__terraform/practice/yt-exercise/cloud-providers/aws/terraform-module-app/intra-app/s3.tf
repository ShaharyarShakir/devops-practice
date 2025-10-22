resource aws_s3_bucket demo_bucket {
  bucket = "${var.env}-${var.bucket_name}"
  tags = {
    "Name" = "My infra bucket"
    "Environment" = var.env
  }
}
