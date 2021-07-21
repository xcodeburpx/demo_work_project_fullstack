import paho.mqtt.client as mqtt


# TODO:
# - modify this function as a Django standalone script
# - change this function to call 

# On connect method - subscribe to all MQTT topics - mostly it will be GPS data
def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe("#")  # Subscribe to all topics, receive any messages published on it


# On message method - receive new message and handle it.
def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    print("Message received-> " + msg.topic + " " + msg.payload.decode('utf-8'))  # Print a received msg

if __name__ == "__main__":
    client = mqtt.Client("data_receiver")  # Create instance of client - data receinver
    client.on_connect = on_connect  # Define callback function for successful connection
    client.on_message = on_message  # Define callback function for receipt of a message
    client.connect('127.0.0.1')     # Connect to local server
    client.loop_forever()  # Start networking daemon