from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_questions = Question.objects.order_by('-publish_date')[:5]
    output = "<br>".join(q.question_text for q in latest_questions)
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("Detail view of the question: %s" % question_id)


def results(request, question_id):
    return HttpResponse("Results of the question: %s" % question_id)


def vote(request, question_id):
    return HttpResponse("Vote on question: %s" % question_id)
