import json
from datetime import datetime
import time
import boto3
from dotenv import dotenv_values

from faker import Faker

faker_instance = Faker(["en_US"])
config = dotenv_values(".env")
ACCESS_KEY = config.get("ACCESS_KEY")
SECRET_KEY = config.get("SECRET_KEY")
ARN = config.get("ARN")
URL_ORDERS = config.get("URL_ORDERS")
URL_PAYMENTS = config.get("URL_PAYMENTS")

client = boto3.client(
    "sqs", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY
)


response1 = client.receive_message(
    QueueUrl=URL_ORDERS,
)

response2 = client.receive_message(
    QueueUrl=URL_PAYMENTS,
)

print(response1)
print(response2)
