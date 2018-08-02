FROM python:alpine

ADD . /code
WORKDIR /code

RUN apk add --upgrade make git

