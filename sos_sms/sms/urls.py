from django.urls import path
from sms import views

app_name = 'sms'

urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.send, name='send'),
]