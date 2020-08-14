from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Question, Choice
from django.urls import reverse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    choice = question.choice_set.first()
    return render(request, 'polls/details.html', {'question': question, 'choice': choice})

def choice(request, question_id, choice_id):
    choice = Choice.objects.get(pk=choice_id)
    return HttpResponse(choice.votes)

def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST('choice'))
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        select_choice.votes +=1
        select_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))