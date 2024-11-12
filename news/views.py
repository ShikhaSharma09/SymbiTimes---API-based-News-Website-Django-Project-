from django.shortcuts import render
from .models import *;
import random

def index(request):
    return render(request,"index.html")

def news(request):
    return render(request,"news.html")

def quiz(request):
    return render(request,"quiz.html",{"start":"no"})

def start_quiz(request):
    return render(request,"quiz.html",{"start":"no"})

attempted = []
attempting = [None]

counter = 0
score = 0

def get_ques(request):
    global attempted
    global attempting
    global counter
    qna = None
    # start = 1
    # end = 10
    if len(attempted) < 10:
        rand_ques_num = random.randint(1,190)
        if rand_ques_num not in attempted:
            attempted.append(rand_ques_num)
            attempting[0]=rand_ques_num
            counter+=1
        else:
            get_ques(request)
    elif len(attempted) >= 10:
        total_score = score
        reset_values()
        return render(request,"quiz.html",{"qna":[""],"score":total_score})
    if qna is None:
        qna = quiz_qna.objects.filter(id = attempting[0])
    return render(request,"quiz.html",{"qna":qna,"counter":counter})

def check_answer(request):
    global score
    correct = ''
    qna = quiz_qna.objects.filter(id=attempting[0])
    answer = "ques"+str(attempting[0])+"ans"
    response = request.POST.get(answer)
    if response == qna[0].ans:
        
        score += 10
        correct = 'yes'
    elif response != None:
        correct = 'no'
    
    return render(request,"quiz.html",{"qna":qna,"response":response,"correct":correct,"counter":counter})

def reset_values():
    attempted.clear()
    attempting[0]=None
    global score
    score = 0
    global counter
    counter = 0
    
def temp_new_quiz(request):
    reset_values()
    return quiz(request)


import requests
import json
def fetch_news(request):
    query = ""
    try:
        query = request.GET.get('search')
    except:
        query = 'India'
        
    api_key = 'b91dfdd697b443388d9a86be657a50df'

    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)

    news_data = response.json()
    articles = news_data.get('articles')
    return render(request, 'news.html', {'news_data': articles})
    
    
def start_ttt(request,score_1=100,score_2=100):
    player1_id = 1
    player2_id = 2
    return render(request,"tic_tac_toe.html",{"p1_id":player1_id,"p2_id":player2_id,"score_1":score_1,"score_2":score_2})



def start_wdle(request):
    wrd_id = random.randint(1,50)
    wd = words.objects.order_by('?').first()
    wrd = wd.word
    return render(request,"wordle.html",{"word":wrd})
    
    

from django.core.mail import send_mail

def contact_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        send_mail(subject, message, email, ['vidhanshkhosla@gmail.com'])
        return render(request, 'index.html')
    
    return render(request,'index.html')