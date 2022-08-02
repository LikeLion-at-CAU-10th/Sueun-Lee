from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

# Create your views here.
from .models import LikeLion

class LikeLionCreateView(CreateView):
    model = LikeLion
    fields = "__all__"
    #fields = ['name', ]
    success_url = "/likelion"

class LikeLionListView(ListView):
    model = LikeLion
    paginate_by = 30
    ordering = ['-name']

class LikeLionUpdateView(UpdateView):
    model = LikeLion
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = "/likelion"

class LikeLionDeleteView(DeleteView):
    model = LikeLion
    success_url="/likelion"

class LikeLionDetailView(DetailView):
    model = LikeLion
    success_url = "/likelion"