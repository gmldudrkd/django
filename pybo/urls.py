from django.urls import path
from . import views
from . import chat
from . import get_list

app_name='pybo'

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('server/', chat.server),
    path('client/', chat.client),
    path('call_api/', get_list.index),
]