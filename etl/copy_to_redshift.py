from sqlalchemy import create_engine
from config import (
    RS_USER,
    RS_PASS,
    RS_DB_NAME,
    RS_HOST,
    AWS_BUCKET_NAME,
    EXPORT_TABLE_NAME,
    FILE_EXTENSION,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    logger,
)

schema = "staging"
key = "s3://{b}/{f}.{e}".format(
    b=AWS_BUCKET_NAME, f=EXPORT_TABLE_NAME, e=FILE_EXTENSION
)
load_sql = [
    """COPY {s}.{t} FROM '{k}' credentials \
        'aws_access_key_id={ki};aws_secret_access_key={sk}' CSV GZIP""".format(
        s=schema,
        t=EXPORT_TABLE_NAME,
        k=key,
        ki=AWS_ACCESS_KEY_ID,
        sk=AWS_SECRET_ACCESS_KEY,
    )
]

with open("/etl/sql/redshift_setup.sql", "r") as sql_file:
    create_sql_list = sql_file.read().split(";")

with open("/etl/sql/process_apps.sql", "r") as sql_file:
    process_sql_list = sql_file.read().split(";")

engine = create_engine(
    "postgresql://{u}:{p}@{h}:5439/{d}".format(
        u=RS_USER, p=RS_PASS, h=RS_HOST, d=RS_DB_NAME
    )
)


def execute(sql):
    with engine.connect().execution_options(autocommit=True) as con:
        for s in sql:
            if s:
                con.execute(s)


def copy_to_redshift(create_sql_list, load_sql, process_sql_list):
    logger.info("Creating redshift tables if not exists")
    execute(create_sql_list)
    logger.info("Copying data from s3 to staging")
    execute(load_sql)
    logger.info("Inserting data into public")
    execute(process_sql_list)


if __name__ == "__main__":
    copy_to_redshift(create_sql_list, load_sql, process_sql_list)
