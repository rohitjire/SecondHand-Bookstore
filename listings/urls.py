from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name='listings'),
    path('<int:pk>/', views.listing, name='listings'),
    path('search/', views.search, name='search'),
]
