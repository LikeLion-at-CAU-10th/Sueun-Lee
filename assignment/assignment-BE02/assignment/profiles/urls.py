from unicodedata import name
from django.urls import path

from .models import *
from profiles.views import *

urlpatterns = [
    path('create-profile/', create_profile, name="create-profile"),
    path('get-profile-all/', get_profile_all, name='get-profile-all'),
    path('get-profile/<int:id>', get_profile, name='get-profile'),
    path('update-profile/<int:id>', update_profile, name='update-profile'),
    path('delete-profile/<int:id>', delete_profile, name='delete-profile'),
]