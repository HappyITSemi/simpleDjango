from django.shortcuts import render


# Create your views here.

def todo_index(request):
    return render(request, 'index.html', {})