from django.shortcuts import render

# Create your views here.
def surveys(request):
	return render(request, "quiz/surveys.html")

def index(request):
	return render(request, "quiz/index.html")

def abortratt1(request):
	return render(request, "quiz/abortratt1.html")

def resultat(request):
	return render(request, "quiz/resultat.html")

