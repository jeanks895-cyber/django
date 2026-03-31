from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_view, name='form'),
    path('result/', views.result_view, name='result'),
]  