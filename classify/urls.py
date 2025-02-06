from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/classify-number/", views.classify_number_api, name="classify_number_api"),
]
