#coding: utf-8
from django.shortcuts import render
quizzes = {
	"Klassiker": {
	"name:" u"Klassiska böcker",
	"description:" u"Hur bra kan du dina klassiker?"
	},
	"fotboll": {
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

def index(request, slug):
	context = {
	"quiz": quizzes[slug],
	"quiz_slug": slug,
	}
	return render(request, "quiz/index.html", context)

def question(request, slug, number):
	context = {
	"question_number": number, 
	"question": u"Hur många bultar har Ölandsbron?",
		"answer1": u"12",
		"answer2": u"66 400",
		"answer3": u"343",
	"quiz_slug": slug,
	}
	return render(request, "quiz/question.html", context)

def resultat(request, slug):
	context = {
	"correct": 12,
	"total": 20,
	"quiz_slug": slug,
	}
	return render(request, "quiz/resultat.html", context)




