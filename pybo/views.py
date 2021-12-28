

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question

import time
from socket import *
import threading

def index(request):
    '''
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
    '''

    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question,id=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)

def server(request):
    serverSock = socket(AF_INET, SOCK_STREAM)
    serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    serverSock.bind(('127.0.0.1', 8080))  # 8080 포트에서 모든 인터페이스(소켓)에게 연결
    serverSock.listen(1)  # 상대방의 접속을 기다림

    connectionSock, addr = serverSock.accept()

    serverSock.close()
    return HttpResponse(str(addr)+'에서 접속하였습니다.')

def client(request):
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('127.0.0.1', 8080))  # 자기자신에게 8080포트로 연결
    clientSock.close()
    return HttpResponse('연결되었습니다.')

