from multiprocessing import context
import re
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse

# Create your views here.

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {'latest_question_list' : latest_question_list}
  return render(request, 'myapp/index.html', context)

def results(request, question_id):
  question = Question(pk=question_id)
  return render(request, 'myapp/results.html', {'question' : question})

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    #vai receber o voto e gravar no database
    selected_choice = question.choice_set.get(pk=request.POST['choice'])

  except KeyError:

    #caso não tenha selecionado uma opção de voto
    return render(request, 'myapp/vote.html', {'question' : question, 'error_message' : 'Selecione uma alternativa'})

  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('myapp:results', args=(question_id,)))

