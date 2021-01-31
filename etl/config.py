import logging
import os
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)
stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)


PG_USER = os.getenv("POSTGRES_USER")
PG_PASS = os.getenv("POSTGRES_PASSWORD")
PG_DB_NAME = os.getenv("POSTGRES_DB")
PG_HOST = "postgres"

SEED_SIZE = 5000000

EXPORT_FOLDER = "/etl/data"
EXPORT_TABLE_NAME = "apps"
FILE_EXTENSION = "csv.gz"

AWS_BUCKET_NAME = "etl"
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

RS_USER = os.getenv("RS_DB_USER")
RS_PASS = os.getenv("RS_DB_PASSWORD")
RS_DB_NAME = os.getenv("RS_DB_NAME")
RS_HOST = os.getenv("RS_DB_HOST")
