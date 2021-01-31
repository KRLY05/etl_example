from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy.dialects.postgresql import INTEGER, VARCHAR, TIMESTAMP
from config import PG_USER, PG_PASS, PG_DB_NAME, PG_HOST, logger

# Schema definition
meta = MetaData()
apps = Table(
    "apps",
    meta,
    Column("pk", INTEGER, primary_key=True, autoincrement=True),
    Column("id", INTEGER),
    Column("title", VARCHAR(256)),
    Column("description", VARCHAR(2000)),
    Column("published_timestamp", TIMESTAMP),
    Column("last_update_timestamp", TIMESTAMP),
)

engine = create_engine(
    "postgresql://{u}:{p}@{h}:5432/{d}".format(
        u=PG_USER, p=PG_PASS, h=PG_HOST, d=PG_DB_NAME
    )
)

if __name__ == "__main__":
    logger.info("Creating apps table")
    meta.create_all(engine)
