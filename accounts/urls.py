from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/confirm', views.confirm_register, name='confirmregister'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/myinquiries', views.myinquiries, name='myinquiries'),
    path('dashboard/inquiries', views.inquiries, name='inquiries'),
    path('dashboard/send_reply', views.send_reply, name='send_reply'),
    path('change_password/',views.change_password,name='change_password')
]
