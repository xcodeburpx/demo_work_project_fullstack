import django
import os
import paho.mqtt.client as mqtt
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'dj_backend_server.settings'
django.setup()

from driver_car_app.tasks import database_parser


# TODO:
# - modify this function as a Django standalone script- DONE
# - change this function to call Celery task - DONE

# On connect method - subscribe to all MQTT topics - mostly it will be GPS data
# The callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc):

    # Print result of connection attempt
    print("Connected with result code {0}".format(str(rc)))

    # Subscribe to all topics, receive any messages published on it
    client.subscribe("+/gps")


# On message method - receive new message and handle it.
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Message received-> " + msg.topic + " " +
                                msg.payload.decode('utf-8'))
    print("Sending to Celery task")
    database_parser.delay([msg.topic, msg.payload.decode('utf-8')])


if __name__ == "__main__":
    # Create instance of client - data receiver
    client = mqtt.Client("data_receiver")

    # Define callback function for successful connection
    client.on_connect = on_connect

    # Define callback function for receipt of a message
    client.on_message = on_message

    # Connect to local server
    client.connect('127.0.0.1')

    # Start networking daemon
    client.loop_forever()
