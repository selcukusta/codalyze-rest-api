FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8
LABEL maintainer="selcukusta@gmail.com"
COPY ./ /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80/tcp
