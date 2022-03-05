
# Create your views here.
import pprint

from django.contrib.sites import requests
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .form import QuestionForm
import requests

import time
from socket import *
import threading

def terminal_info(request):

    url = 'http://openapi.tago.go.kr/openapi/service/ExpBusInfoService/getStrtpntAlocFndExpbusInfo'
    params ={
        'serviceKey' : '2VHxUF1kGVgQCm34HiA23zKHV1DzYB92jG9FyirJu0Y4WsvsrGsRl89ZLLI7uMawtjfDJKXkPztHHGD+lLPoug==', 'numOfRows' : '10', 'pageNo' : '1', 'depTerminalId' : 'NAEK010', 'arrTerminalId' : 'NAEK300', 'depPlandTime' : '20200101', 'busGradeId' : '1'
    }

    response = requests.get(url, params=params)
    '''contents = response.text

    dataPrint = pprint.PrettyPrint'''

    return HttpResponse(response)


def train_info(request):

    url = 'http://openapi.tago.go.kr/openapi/service/TrainInfoService/getStrtpntAlocFndTrainInfo'
    params ={
        'serviceKey' : '2VHxUF1kGVgQCm34HiA23zKHV1DzYB92jG9FyirJu0Y4WsvsrGsRl89ZLLI7uMawtjfDJKXkPztHHGD+lLPoug==', 'numOfRows' : '10', 'pageNo' : '1', 'depPlaceId' : 'NAT010000', 'arrPlaceId' : 'NAT011668', 'depPlandTime' : '20201201', 'trainGradeCode' : '00'
    }

    response = requests.get(url, params=params)
    '''contents = response.text

    dataPrint = pprint.PrettyPrint'''

    return HttpResponse(response)
