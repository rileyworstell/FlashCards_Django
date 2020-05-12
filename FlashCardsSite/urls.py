from django.contrib import admin
from django.urls import path
from FlashCards import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('create/', views.createCard, name='createCard'),
    path('logout/', views.logoutuser, name="logoutuser"),
    path('login/', views.loginuser, name="loginuser"),
    
    #Auth
    path('signup/', views.signupuser, name="signupuser"),

]
