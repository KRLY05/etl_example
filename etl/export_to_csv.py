import csv
import gzip

from sqlalchemy import create_engine
from config import (
    PG_USER,
    PG_PASS,
    PG_DB_NAME,
    PG_HOST,
    logger,
    EXPORT_TABLE_NAME,
    EXPORT_FOLDER,
    FILE_EXTENSION,
)


def export_to_csv(table):
    logger.info("Unloading data from apps table into csv file")
    engine = create_engine(
        "postgresql://{u}:{p}@{h}:5432/{d}".format(
            u=PG_USER, p=PG_PASS, h=PG_HOST, d=PG_DB_NAME
        )
    )
    conn = engine.connect()
    sql = "SELECT id, title, description, published_timestamp, last_update_timestamp  FROM {}".format(
        table
    )
    result = conn.execute(sql)
    with gzip.open(
        "{}/{}.{}".format(EXPORT_FOLDER, EXPORT_TABLE_NAME, FILE_EXTENSION), "wt"
    ) as file:
        a = csv.writer(file)
        a.writerows(result)
    conn.close()


if __name__ == "__main__":
    export_to_csv(EXPORT_TABLE_NAME)
