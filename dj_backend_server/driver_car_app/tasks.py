from celery.decorators import task
from celery.utils.log import get_task_logger
from .models import Truck, Gps

from datetime import datetime
logger = get_task_logger(__name__)

# Celery task - collect data and save to database
@task(name='database_parser')
def database_parser(data: list) -> None:

    # Unpack the data
    mqtt_topic, gps_data = data[0], data[1]
    car_name = mqtt_topic.split("/")[0]

    # Search for a proper truck
    truck = Truck.objects.filter(truck_name__iexact=car_name).first()

    # If truck was found - create new GPS record:
    if(truck):
        # Split gps data string
        gps_data = gps_data.split("|")

        # Calculate proper timestamp
        timestamp = int(gps_data[0])
        timestamp = datetime.fromtimestamp(timestamp)

        # Convert string data to float
        longitude = float(gps_data[1])
        latitude = float(gps_data[2])
        altitude = float(gps_data[3])

        # Create new Gps object
        gps_record = Gps(timestamp=timestamp, truck=truck, longitude=longitude,
                         latitude=latitude, altitude=altitude)

        # Save the record
        gps_record.save()

    else:
        print(f"Truck {car_name} was not found in database! Skipping Gps record")
