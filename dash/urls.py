from django.urls import path
from . import views

app_name = 'dash'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('adminPage/', views.adminPage, name='adminPage'),
    path('logout/', views.user_logout, name='logout')

]