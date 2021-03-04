FROM python:3.7
EXPOSE 8000

RUN apt-get update && apt-get install -y cron

WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app
RUN mkdir /app/tmp

RUN chmod +x scripts/run-prod.sh
CMD scripts/run-prod.sh