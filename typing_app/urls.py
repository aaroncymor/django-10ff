from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_result/', views.save_result, name='save_result'),
]
