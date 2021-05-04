from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/confirm', views.confirm_register, name='confirmregister'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard')
]
