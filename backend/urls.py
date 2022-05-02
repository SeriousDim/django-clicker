from django.urls import path

from backend import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path("index/", views.index, name="index")
]