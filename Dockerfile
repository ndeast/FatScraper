FROM python:alpine3.15

RUN apk add --update sqlite

# Install Dependencies 
COPY ./requirements.txt /FatScraper/requirements.txt
RUN pip install -r /FatScraper/requirements.txt

COPY . /FatScraper/