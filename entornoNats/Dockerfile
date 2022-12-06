FROM python:3.8-alpine3.13

WORKDIR /data
COPY ./app.py /data
RUN pip install nats-py

CMD ["python3", "app.py"]
