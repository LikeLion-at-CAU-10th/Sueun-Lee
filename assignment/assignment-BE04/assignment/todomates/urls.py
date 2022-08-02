from unicodedata import name
from django.urls import path

from todomates.views import create_category, create_todo, get_category, get_category_all


urlpatterns = [
    path('create-category/', create_category, name="create_category"),
    path('get_category_all/', get_category_all, name="get_category_all"),
    path('get_category/<int:id>', get_category, name="get_category"),
    path('create_todo/<int:category_id>', create_todo, name="create_todo"),
]