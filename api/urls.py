from django.urls import path

from api import views

urlpatterns = [
    path('note/', views.NoteView.as_view(), name='note'),
    path('reg/', views.Register.as_view(), name='reg')
]