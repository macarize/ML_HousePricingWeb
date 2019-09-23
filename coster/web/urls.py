from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('consultantTest', views.consultantTest, name='consultantTest'), # 테스트
    path('login', views.login, name='login'),
    path('find', views.find, name='find'),
    path('Hub', views.Hub, name='Hub'),
    path('Intro', views.Intro, name='Intro'),
    path('consultant', views.consultant, name='consultant'),
]