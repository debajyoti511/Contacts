from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('user_login', user_login, name='user_login'),
    path('user_logout', user_logout, name='user_logout'),
    path('create_contact', create_contact, name='create_contact'),
    path('display<pk>', display, name='display'),
    path('update<pk>', update, name='update'),
    path('delete<pk>', delete, name='delete'),
    path('search', search, name='search'),
    path('un', un, name='un'),
    path('otp', otp, name='otp'),
    path('change_pw', change_pw, name='change_pw'),
    path('change_new_password', change_pw, name='change_new_password'),
    path('login_with_otp', login_with_otp, name='login_with_otp'),
    path('loginotp', loginotp, name='loginotp')
]
