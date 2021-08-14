from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class GpsConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.room_group_name = "main"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from room group
    def gps_message(self, event):
        message = event['message']
        # print("Gps Data: {message}")
        # print(f"Gps data type: {type(message)}")
        gps_data = json.loads(message)

        # print("Gps Data 2: {gps_data}")
        # print(f"Gps data 2 type: {type(gps_data)}")
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'gps_data': gps_data
        }))
