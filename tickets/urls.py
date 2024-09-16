from django.urls import path
from  .views.login import login_view
from  .views.register import register
from  .views.home import home
from  .views.admin_user import admin_user
from  .views.redirected import redirected, logout_view
from  .views.home_user import home_user
from  .views.home_user_tickets import home_user_tickets

urlpatterns = [
    
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('redirected', redirected, name='redirected' ), #url para redireccionar a la pagina corresp. segun rol
    

    path('my-tickets/', home_user_tickets, name='home_user_tickets'), #Url cuando el user da el boton de ver ticket creados en home_user
    path('home_user/', home_user, name='home_user'),  #
    #path('home_support1/', home_user, name='home_support1'), 
    #path('home_support2/', home_user, name='home_support2'), 
    path('logout/', logout_view, name='logout'), #logout
    path('admin_user/', admin_user, name='admin_user')
]

