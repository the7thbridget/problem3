from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='web-home'),
    path('data/', views.data, name='data')
]
