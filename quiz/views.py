from django.shortcuts import render

# Create your views here.
def startpage(request):
return render(request, “quiz/surveys.html”)
def quiz(request):
return render(request, “quiz/index.html”)
def question(request):
return render(request, “quiz/abortratt1.html”)
def completed(request):
return render(request, “quiz/resultat.html”)

