from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/confirm', views.confirm_register, name='confirmregister'),
]