from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('signup', views.signup, name='signup'),
    # path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('consultant', views.consultant, name='consultant'),
    path('login', views.login, name='login'),
    path('find', views.find, name='find'),
]