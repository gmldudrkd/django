
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

def index(request):
    '''
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
    '''

    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

    '''return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")'''


def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id=question_id)

def question_created(request):
    " 질문등록 "
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            "form에서 넘어온 값을 임시저장 False - create_date 값이 없어 db저장에 오류가 발생"
            question = form.save(commit=False)
            "create_date 값을 저장당시 시간으로 저장"
            question.create_date = timezone.now()
            "실제 db에 저장"
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
        context = {'form' :form}
        return render(request, 'pybo/question_form.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question ,id=question_id)
    context = {'question' :question}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCH5HHuysBCaw-kMd_SjSxCFM9un3Kun0Y'
    data = {
        'considerIp': True,
    }
    result = requests.post(url, data=data)
    return HttpResponse(result)


