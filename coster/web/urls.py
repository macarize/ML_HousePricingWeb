from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('Hub', views.Hub, name='Hub'),
    path('Intro', views.Intro, name='Intro'),
    path('consultant', views.consultant, name='consultant'),
    path('si', views.si, name='si'),
    path('gu', views.gu, name='gu'),
    path('Results', views.Results, name='Results'),
    path('Seller', views.Seller, name='Seller'),
    path('submit', views.submit, name='submit'),
    path('middlemanAjax', views.middlemanAjax, name='middlemanAjax'),
]