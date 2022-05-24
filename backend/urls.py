from django.urls import path

from backend import views

boosts = views.BoostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path("call_click/", views.call_click),
    path('', views.index, name='index'),
    path('boosts/', boosts, name="boosts"),
    path('logout/', views.user_logout, name='logout'),
    path('buy_boost/<int:id>', views.buy_boost, name="buy_boost")
]