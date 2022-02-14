from django.contrib.sites import requests
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .form import QuestionForm
import requests

def index(request):
    return render(request, 'call/index.html', {})