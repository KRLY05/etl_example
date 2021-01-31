FROM python:3
ADD etl/requirements.txt /etl/requirements.txt
WORKDIR /etl
RUN apt-get update
RUN pip install -r requirements.txt