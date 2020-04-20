from django.urls import path
from .views import *
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', home, name='home'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', login_required(logout_then_login), name='logout')
]