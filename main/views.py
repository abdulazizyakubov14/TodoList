
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from .models import *

# Create your views here.
class HomeView(ListView):
    model = TodoList

class DetaiPage(DetailView):
    model = TodoList
    slug_field = 'slug'
    template_name = 'detail.html'

class CreatTodo(CreateView):
    model = TodoList
    fields = ['title','body','image','prioroty','star']
    success_url = '/'

class DeletPage(DeleteView):
    model = TodoList
    success_url = '/'
