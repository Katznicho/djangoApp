from django.urls import path
from . import views

#url config module
urlpatterns = [
    path('hello/', views.say_Hello)
]