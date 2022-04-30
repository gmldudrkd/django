from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.sites import requests
import json

# 웹소켓 처리를 위한 핸들러 클래스
class ChatConsumer(WebsocketConsumer):

    # 사용자와 웹소켓 연결이 맺어졌을때 호출
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    # 사용자와 웹소켓 연결이 끊어졌을때 호출
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # 사용자가 메시지를 보내면 호출 됨
    # WebSocket 에게 메세지 receive
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # room group 에게 메세지 send
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': self.room_group_name+" : "+message
            }
        )

    # room group 에서 메세지 receive
    def chat_message(self, event):
        message = event['message']
        # websocket 에게 메세지 전송
        self.send(text_data=json.dumps({
            'message': message,
            'answer' : 'Server : Hello'
        }))