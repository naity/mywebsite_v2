from django.urls import path

from . import views


app_name = "photography"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('like_photo/', views.like_photo, name="like_photo"),
]