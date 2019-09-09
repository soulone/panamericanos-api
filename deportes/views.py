from django.template import loader
from django.shortcuts import render
from .models import Deporte
from django.utils import timezone
from django.http import HttpResponse
from django.http import Http404

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def index(request):
    deportes=Deporte.objects.all()
    return render(request, 'deportes/index.html',{'deportes':deportes})

