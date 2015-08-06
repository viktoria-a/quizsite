#coding: utf-8
from django.shortcuts import render
quizzes = {
	"Klassiker": {
	"name:" u"Klassiska böcker",
	"description:" u"Hur bra kan du dina klassiker?"
	},
	"Fotboll": {
	"name:" u"Största fotbollslagen",
	"description" u"Kan du dina lag?"
	},
	"Kanada-hackare": {
	"name:" u"Världens mest kända hackare",
	"description:" u"Hacker-historia är viktigt, kan du den?"
	},
}

# Create your views here.
def surveys(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/surveys.html", context)

def index(request):
	return render(request, "quiz/index.html")

def abortratt1(request):
	return render(request, "quiz/abortratt1.html")

def resultat(request):
	return render(request, "quiz/resultat.html")



