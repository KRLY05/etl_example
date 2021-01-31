import boto3

from config import (
    EXPORT_FOLDER,
    EXPORT_TABLE_NAME,
    FILE_EXTENSION,
    AWS_BUCKET_NAME,
    logger,
)

file_path = "{}/{}.{}".format(EXPORT_FOLDER, EXPORT_TABLE_NAME, FILE_EXTENSION)
key = "{}.{}".format(EXPORT_TABLE_NAME, FILE_EXTENSION)


def upload_to_s3(file, bucket_name, key):
    logger.info("Uploading {} to S3 bucket {}".format(file, bucket_name))
    s3 = boto3.resource("s3")
    s3.meta.client.upload_file(file, bucket_name, key)


if __name__ == "__main__":
    upload_to_s3(file_path, AWS_BUCKET_NAME, key)
