#coding: utf-8
from django.shortcuts import render
from quiz.models import Quiz

# Create your views here.
def surveys(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/quizzes.html", context)

def quiz(request, slug):
	context = {
	"quiz": Quiz.objects.get(slug=slug),
	}
	return render(request, "quiz/quiz.html", context)

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




