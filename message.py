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

client = boto3.client(
    "sns", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY
)


def get_data():
    lat, lng, region, country, timezone = faker_instance.location_on_land()
    return dict(
        created_at=f"{datetime.utcnow()}",
        updated_at=f"{datetime.utcnow()}",
        customer_id=faker_instance.uuid4(),
        name=faker_instance.name(),
        region=region,
        country=country,
        lat=lat,
        lng=lng,
        email=faker_instance.ascii_free_email(),
        phone=faker_instance.phone_number(),
    )


while True:
    data = get_data()
    client.publish(
        TopicArn=ARN,
        Message=json.dumps(data),
    )

    print(data)
    time.sleep(5)
