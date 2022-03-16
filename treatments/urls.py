from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_treatments, name='treatments'),
    path('eye_care/', views.eye_care, name='eye_care'),
    path('nail_care/', views.nail_care, name='nail_care'),
    path('facial/', views.facial, name='facial'),
]
