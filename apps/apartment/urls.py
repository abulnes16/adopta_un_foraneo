from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('property-detail/<int:id>', apartment_detail, name='details'),
    path('add_coment/<int:id>', add_coment, name='comment')
]