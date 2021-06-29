from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('create/', CreatTodo.as_view(), name="create"),
    path('detail/<slug:slug>/', DetaiPage.as_view(), name="details"),
    path('delet/<pk>/', DeletPage.as_view(), name="delets"),

]