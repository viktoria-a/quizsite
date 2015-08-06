from django.conf.urls import url
from quiz import views
urlpatterns = [
    url("^$", views.surveys),
    url(r"^quiz/[a-z-]+/$", views.index),
    url(r"^quiz/[a-z-]+/question/[0-9]/$", views.abortratt1),
    url(r"^quiz/[a-z-]+/completed/$", views.resultat),
]
