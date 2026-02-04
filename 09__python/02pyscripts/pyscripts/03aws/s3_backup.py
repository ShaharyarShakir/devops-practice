"""
Create a aws IAM user with S3 access.
configure the AWS CLI with the access key and secret key of the user.
import boto3 using uv
"""

import boto3

# Explicitly specify the region
session = boto3.session.Session(region_name="us-east-1")  # or any other region
s3 = session.resource("s3")


def list_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)


def create_bucket(s3, bucket_name):
    region = s3.meta.client.meta.region_name

    if region == "us-east-1":
        s3.create_bucket(Bucket=bucket_name)
    else:
        s3.create_bucket(
            Bucket=bucket_name, CreateBucketConfiguration={"LocationConstraint": region}
        )
    print(f"Bucket {bucket_name} created successfully.")


def upload_backup(s3, file_name, bucket_name, key_name):
    data = open(file_name, "rb")
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print(f"File {file_name} uploaded to bucket {bucket_name} with key {key_name}.")
    print("Backup uploaded successfully.")


bucket_name = "demo-python-bucket-unique-12345678"
file_name = "/home/shaharyar/git-repos/devops-practice/09__python/02pyscripts/pyscripts/03aws/backups/backup_2025-06-28 08:24:39.906753.tar.gz"
key_name = "backup_2025-06-28.tar.gz"
upload_backup(s3, file_name, bucket_name, key_name)


# list_buckets(s3)
# create_bucket(s3, 'demo-python-bucket-unique-12345678')
