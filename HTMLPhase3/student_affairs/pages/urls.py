from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_of_all,name='first_of_all'),
    path('home/', views.home_page, name='home_page'),
    path('signin/', views.sign_in, name='sign_in'),
]