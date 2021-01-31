## ETL job example
   Example of simple ETL job
   
   Job transfers data from Postgres to Redshift

### Requirements
 - [Docker](https://docs.docker.com/install/)
 - [Docker Compose](https://docs.docker.com/compose/install/)
 - [Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html)
 - [S3](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) Create bucket `etl` (or set your bucket name in `congig.py`)
 
### Deploy

- fill in `etl.env` with your AWS and Redshift credentials

- run `make deploy`

### Execute job

To execute the whole job, run  `make run_etl`

ETL job consists of the following steps, each can be triggered separately:

- Creating tables in source database (postgres)
    
    `make create_tables`

- Seeding source database with random data (seed size can be adjusted in `config.py`)

    `make seed_db`

- Exporting data from source database to local csv file

    `make export_csv`

- Uploading file to s3 bucket

    `make upload_s3`

- Copying data from s3 to Redshift

    `make copy_rs`

## PySpark job example
   
   Simple example of word count job using PySpark

### Execute job
    
The easiest way to demonstrate execution of pyspark scipt is to run it in pyspark Docker container with jupyter notebook

- start the container: `make pyspark`
- Go to http://127.0.0.1:8888 followed by token according to instructions in terminal
- Start the notebook work/wordcount.ipynb
- Copy input data file into ./pyspark folder
- Run the code in the notebook

## SQL and JQ example

Directory `sql_and_jq` contains:

- examples of ddl and select query for apps table
- example of json transform script using JQ
