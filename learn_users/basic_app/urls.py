from django.contrib import admin
from django.urls import include, path
from basic_app import views

app_name =  'basic_app'
urlpatterns = [

    path('', views.index, name='index'),
    path('', views.register, name='register'),
    path('user_login', views.user_login, name = 'user_login')
]
