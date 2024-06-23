from django.urls import path
from .import views

urlpatterns=[
    path('', views.home, name='info-home'),
    path('farming/', views.farming, name='info-farming'),
    path('disease/', views.disease, name='info-disease'),
]