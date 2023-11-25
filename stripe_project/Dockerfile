# pull official base image
FROM python:3.11-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
RUN mkdir /web
WORKDIR /web

RUN apk update && apk upgrade \
    && apk add --no-cache \
        postgresql-dev \
        gcc \
        python3-dev \
        musl-dev

COPY bootstrap.sh .
COPY requirements requirements/
RUN pip install --upgrade pip \
    && pip install -r requirements/local.txt

RUN chmod +x ./bootstrap.sh

# copy project
COPY . .