from sqlalchemy import create_engine
from config import PG_USER, PG_PASS, PG_DB_NAME, PG_HOST, SEED_SIZE, logger

seed_sql = """INSERT INTO apps(id,title,description,published_timestamp,last_update_timestamp)
    SELECT tab.col,
    left(md5(random()::text),5),
    md5(random()::text),
    '2020-01-01'::timestamp - random() * interval '1 year',
    '2020-01-01'::timestamp + random() * interval '1 year'
    FROM generate_series(1,{}) tab(col)""".format(
    SEED_SIZE
)


def seed_db(sql):
    logger.info("Generating {} rows".format(SEED_SIZE))
    engine = create_engine(
        "postgresql://{u}:{p}@{h}:5432/{d}".format(
            u=PG_USER, p=PG_PASS, h=PG_HOST, d=PG_DB_NAME
        )
    )
    with engine.connect() as con:
        con.execute(sql)


if __name__ == "__main__":
    seed_db(seed_sql)
