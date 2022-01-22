import time
from socket import *
import threading

from django.contrib.sites import requests

from .form import QuestionForm
from django.http import HttpResponse
from django.shortcuts import render

def server(request):
    serverSock = socket(AF_INET, SOCK_STREAM)
    serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    serverSock.bind(('127.0.0.1', 8080))  # 8080 포트에서 모든 인터페이스(소켓)에게 연결
    serverSock.listen(1)  # 상대방의 접속을 기다림

    connectionSock, addr = serverSock.accept()

    serverSock.close()
    # return HttpResponse(str(addr)+'에서 접속하였습니다.')
    context = {
        'type' : 'server',
        'context': str(addr)+'에서 접속하였습니다.',
        'welcome' : '안녕하세요. 원하시는 정보를 입력해주세요.'
    }

    """
    # target : 스레드 실행함수, args : 함수에 전달할 인자자 > (var,)로 입력해야 튜플로 인지
    sender = threading.Thread(target=send, args=(connectionSock,))
    receiver = threading.Thread(target=receive, args=(connectionSock,))

    sender.start()
    receiver.start()
    """
    return render(request, 'chat/chat_detail.html', context)

def client(request):
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('127.0.0.1', 8080))  # 자기자신에게 8080포트로 연결
    clientSock.close()
    #return HttpResponse('연결되었습니다.')
    context = {
        'type': 'client',
        'context': '연결되었습니다.',
        'welcome': '안녕하세요. 원하시는 정보를 입력해주세요.'
    }

    """
    sender = threading.Thread(target=send, args=(clientSock,))
    receiver = threading.Thread(target=receive, args=(clientSock,))

    sender.start()
    receiver.start()
    """

    return render(request, 'chat/chat_detail.html', context)

def answer_create(request):
    form = QuestionForm(request.POST)
    context = {'answer': form}
    return render(request, 'chat/chat_detail.html', context)

def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 : ', recvData.decode('utf-8'))
