from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/confirm', views.confirm_register, name='confirmregister'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/myinquiries', views.myinquiries, name='myinquiries'),
    path('dashboard/inquiries', views.inquiries, name='inquiries'),
    path('dashboard/send_reply', views.send_reply, name='send_reply'),
    path('change_password/', views.change_password, name='change_password'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='accounts/reset.html'),
         name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_done.html'),
         name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_complete.html'),
         name='password_reset_complete')
]
