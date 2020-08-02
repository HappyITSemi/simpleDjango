from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.TodoIndexView.as_view(), name='index'),
    path('input_menu/', views.PostMenuView.as_view(), name='input_menu'),
]
