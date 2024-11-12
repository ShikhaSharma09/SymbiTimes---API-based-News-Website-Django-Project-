from django.db import models

class quiz_qna(models.Model):
    idx = models.IntegerField()
    ques = models.CharField(max_length=300)
    opt1 = models.CharField(max_length=100)
    opt2 = models.CharField(max_length=100)
    opt3 = models.CharField(max_length=100)
    opt4 = models.CharField(max_length=100)
    ans = models.CharField(max_length=100)

class words(models.Model):
    idx = models.IntegerField()
    word = models.CharField(max_length=300)