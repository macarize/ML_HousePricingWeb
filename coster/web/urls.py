from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('find', views.find, name='find'),
    path('Hub', views.Hub, name='Hub'),
    path('Intro', views.Intro, name='Intro'),
    path('consultant', views.consultant, name='consultant'),
    path('si', views.si, name='si'),
    path('gu', views.gu, name='gu'),
    path('Results', views.Results, name='Results'),
    path('Seller', views.Seller, name='Seller'),
]