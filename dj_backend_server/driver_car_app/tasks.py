import json
from re import search
from celery.decorators import task
from celery.utils.log import get_task_logger
from django.forms.models import model_to_dict
from .models import Truck, Gps
from django.core import serializers

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from datetime import datetime
logger = get_task_logger(__name__)

# Celery task - collect data and save to database
@task(name='database_parser')
def database_parser(data: list) -> None:

    # Unpack the data
    mqtt_topic, gps_data = data[0], data[1]
    car_name = mqtt_topic.split("/")[0]

    gps_wb_data = dict()
    gps_wb_data['truck'] = car_name


    # Search for a proper truck
    truck = Truck.objects.filter(truck_name__iexact=car_name).first()

    # If truck was found - create new GPS record:
    if(truck):
        # Split gps data string
        gps_data = gps_data.split("|")

        # Calculate proper timestamp
        timestamp = int(gps_data[0])
        timestamp = datetime.fromtimestamp(timestamp)
        gps_wb_data['timestamp'] = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        # Convert string data to float
        longitude = float(gps_data[2])
        latitude = float(gps_data[1])
        altitude = float(gps_data[3])
        
        gps_wb_data['longitude'] = longitude
        gps_wb_data['latitude'] = latitude
        gps_wb_data['altitude'] = altitude

        # Create new Gps object
        gps_record = Gps(timestamp=timestamp, truck=truck, longitude=longitude,
                         latitude=latitude, altitude=altitude)

        # Save the record
        gps_record.save()

        # Send record to Websocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'main',
            {
                    'type': 'gps_message',
                    'message': json.dumps(gps_wb_data)
            }
        )

    else:
        print(f"Truck {car_name} was not found in database! Skipping Gps record")
