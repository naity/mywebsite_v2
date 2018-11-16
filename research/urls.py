from django.urls import path

from . import views


app_name = "research"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('count_downloads/', views.count_downloads, name="count_downloads"),
]