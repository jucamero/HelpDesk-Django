from django.urls import path
from  .views.home_user import home_user, logout_view
from  .views.login import login_view
from  .views.register import register
from  .views.home import home


urlpatterns = [
    
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('home_user/', home_user, name='home_user'), 
    path('logout/', logout_view, name='logout'),  
]

