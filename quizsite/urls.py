from django.conf.urls import url
from quiz import views
urlpatterns = [
	url("^$", views.surveys, name="surveys_page"),
	url(r"^quiz/([a-z-]+)/$", views.index, name="index_page"),
	url(r"^quiz/([a-z-]+)/question/([0-9]+)/$", views.question, name="question_page"),
	url(r"^quiz/([a-z-]+)/completed/$", views.resultat, name="resultat_page"),
	]
