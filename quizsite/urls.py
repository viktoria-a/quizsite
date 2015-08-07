from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import url
from quiz import views
urlpatterns = [
	url("^$", views.quizzes, name="quizzes_page"),
	url(r"^quiz/([a-z-]+)/$", views.quiz, name="quiz_page"),
	url(r"^quiz/([a-z-]+)/question/([0-9]+)/$", views.question, name="question_page"),
	url(r"^quiz/([a-z-]+)/completed/$", views.resultat, name="resultat_page"),
	url(r'^admin/', include(admin.site.urls)),
	]
