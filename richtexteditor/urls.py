from django.urls import path
from . import views

app_name = 'richtexteditor'

urlpatterns = [
    path('create', views.create_post, name='create'),
    path('home', views.home, name='home')
]