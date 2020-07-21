#
from django.shortcuts import render
from django.urls import path
from . import views


def todo_index(request):
    return render(request, 'todos/index.html', {})


app_name = 'todos'

urlpatterns = [
    path('', todo_index, name='todo_index')
]
