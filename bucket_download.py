import boto3
import os

s3 = boto3.client('s3')
bucket_name = 'bucket'
region = 'eu-north-1'


def download_bucket(bucket_name, local_dir='.'):
    print(f"Downloading contents of {bucket_name} to {local_dir}")

    paginator = s3.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket_name):
        for obj in page.get('Contents', []):
            file_key = obj['Key']
            file_path = os.path.join(local_dir, file_key)

            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            print(f"Downloading {file_key}")
            s3.download_file(bucket_name, file_key, file_path)

    print(f"\nDownload completed!")


if __name__ == '__main__':
    # list_bucket_contents(bucket_name)

    download_bucket(bucket_name, local_dir='E:/script_sales_bucket_download/downloaded_content/aws-sam-cli-managed')
