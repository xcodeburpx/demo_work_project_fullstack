import paho.mqtt.client as mqtt
import argparse
import random
import time

# Argument list parser - for simplicity
def argument_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("car_name", help="Name of the car that will be used in spoofer")
    parser.add_argument("--timedelta", 
                        help="Time in seconds, which indicates how much time is between messages",
                        type=int,
                        default=3)
    arg_list = parser.parse_args()

    return arg_list


# Random GPS location function
def gps_random_location() -> str: 
    print("[gps_random_location] Generating GPS data")
    timestamp = str(int(time.time()))
    latitude = str(random.uniform(-90,90))
    longitude = str(random.uniform(-180,180))
    altitude = str(random.uniform(0,8100))

    return "|".join([timestamp, latitude, longitude, altitude])


# Main function
def send_gps_data(car_name: str, timedelta: int) -> None:
    # Initialize MQTT spoofer
    print("[send_gps_data] Initialize client and connect with broker")
    client = mqtt.Client("data_spoofer_{}".format(car_name))
    client.connect("127.0.0.1")

    # Loop and send information to MQTT topic
    # If Ctrl + C - close program
    # Else - raise Exception
    while True:
        try:
            print("[send_gps_data] Collect GPS data")
            gps_data = gps_random_location()
            print("[send_gps_data] Send GPS data")
            client.publish("{}/gps".format(car_name), "{}".format(gps_data))
            print("[send_gps_data] Sleep for {} seconds".format(timedelta))
            time.sleep(timedelta)
        except KeyboardInterrupt:
            print("[send_gps_data] Script ends execution by keyboard interrupt signal")
            client.disconnect()
            break
        except Exception as e:
            client.disconnect()
            raise Exception("[send_gps_data] Script failed for some reason: {}".format(e))


if __name__ == "__main__":
    arg_list = argument_list()
    print("[main] passed arguments: {}".format(arg_list))
    send_gps_data(arg_list.car_name, arg_list.timedelta)
