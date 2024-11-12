from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('index',index,name='index'),
    path('news',news,name='news'),
    path('start_quiz',start_quiz,name='start_quiz'),
    path('get_ques',get_ques,name='get_ques'),
    path('check_answer',check_answer,name='check_answer'),
    path('reset_values',reset_values,name='reset_values'),
    path('temp_new_quiz',temp_new_quiz,name='temp_new_quiz'),
    path('fetch_news',fetch_news,name='fetch_news'),
    path('start_ttt',start_ttt,name='start_ttt'),
    path('start_wdle',start_wdle,name='start_wdle'),
    path('contact_view',contact_view,name='contact_view'),
]