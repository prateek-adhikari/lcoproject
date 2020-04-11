from django.urls import path
from lco import views
urlpatterns = [
    path('', views.home, name="home"),
    path('team', views.team, name="team"),
    path('tournament', views.tournament, name="tournament"),
    path('faq', views.faq, name="faq"),
    path('about', views.about, name="about"),
]
