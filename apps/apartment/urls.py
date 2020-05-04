from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('profile/update', update_profile, name='update')
]