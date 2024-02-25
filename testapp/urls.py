from django.urls import path
from . import views


urlpatterns = [
    path('user/', views.UserView, name='users_list'),
    path('input/', views.input, name='input'),
    path('save_user/', views.save_user, name='save_user'),
]
