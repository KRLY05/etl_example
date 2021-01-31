.PHONY: build up deploy remove sh create_tables seed_db export_csv upload_s3 copy_rs run_etl pyspark

build:
	docker build --rm -t etl .

up:
	docker-compose -f docker-compose.yml up -d

deploy: build up
	docker ps

remove:
	docker stop $(shell docker ps -a -q)
	docker rm $(shell docker ps -a -q)

rmi:
	docker rmi $(shell docker images -a -q)

sh:
	docker exec -i -t $(shell docker ps -q --filter ancestor=etl) /bin/bash

create_tables:
	docker exec -i -t etl python create_pg_tables.py

seed_db:
	docker exec -i -t etl python seed_db.py

export_csv:
	docker exec -i -t etl python export_to_csv.py

upload_s3:
	docker exec -i -t etl python upload_to_s3.py

copy_rs:
	docker exec -i -t etl python copy_to_redshift.py

run_etl: create_tables seed_db export_csv upload_s3 copy_rs

pyspark:
	docker pull jupyter/pyspark-notebook
	docker run -it --rm -p 8888:8888 -v $(shell pwd)/pyspark:/home/jovyan/work jupyter/pyspark-notebook
