from unicodedata import name
from django.urls import path
from .views import LikeLionCreateView, LikeLionDetailView, LikeLionListView, LikeLionUpdateView, LikeLionDeleteView

urlpatterns = [
    path('create/', LikeLionCreateView.as_view(), name="Likelion_create"),
    path('list/', LikeLionListView.as_view(), name="Likelion_list_all"),
    path('update/<int:pk>/', LikeLionUpdateView.as_view(), name="Likelion_update"),
    path('delete/<int:pk>/', LikeLionDeleteView.as_view(), name="Likelion_delete"),
    path('detail/<int:pk>/', LikeLionDetailView.as_view(), name="Likelion_detail"),
]