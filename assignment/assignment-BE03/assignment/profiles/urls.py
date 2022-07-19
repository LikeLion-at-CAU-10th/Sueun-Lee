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
    path('create_url/<int:profile_id>', create_url, name="create_url"),
    path('get_url_all/<int:profile_id>', get_url_all, name="get_url_all"),
]
