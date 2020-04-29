from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz, Question, Answer, UserAnswer
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import Count, Sum
from django.views.generic import CreateView, ListView, UpdateView
from django.views import View

# Create your views here.

def index(request):
    return HttpResponse("Hello World!!")

def detail(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You'r looking at the results of question %s"
    return HttpResponse(response % question_id)

        #def answer(request, question_id):
        #if(Answer.is_correct == UserAnswer.answer):
#score = score + 1


