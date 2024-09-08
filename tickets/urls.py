from django.urls import path
from  .views.home_user import home_user, logout_view
from  .views.login import login_view
from  .views.register import register
from  .views.home import home
from  .views.admin_user import admin_user

urlpatterns = [
    
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('home_user/', home_user, name='home_user'), 
    path('home_support1/', home_user, name='home_support1'), 
    path('home_support2/', home_user, name='home_support2'), 
    path('logout/', logout_view, name='logout'),  
    path('admin_user/', admin_user, name='admin_user'),  
]

