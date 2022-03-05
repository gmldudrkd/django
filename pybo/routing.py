from django.urls import re_path
from django.conf.urls import url
from . import consumer

websocket_urlpatterns = [
    url(r'^ws/pybo/(?P<room_name>[^/]+)/$', consumer.ChatConsumer),
]