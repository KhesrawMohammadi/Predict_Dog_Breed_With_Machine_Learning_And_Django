from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_breed, name='predict_breed'),
]
