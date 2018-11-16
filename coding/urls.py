from django.urls import path

from . import views


app_name = "coding"
urlpatterns = [
    path('', views.index, name='index'),
]