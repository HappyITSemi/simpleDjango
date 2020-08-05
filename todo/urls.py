from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.TodoIndexView.as_view(), name='index'),
    path('list/', views.TodoListView.as_view(), name='list'),
    path('detail/<int:id>', views.TodoDetailView.as_view(), name='detail'),
    path('create/', views.TodoCreateView.as_view(), name='create'),
    path('update/<int:id>', views.TodoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.TodoDeleteView.as_view(), name='delete'),

    path('input_menu/', views.PostMenuView.as_view(), name='input_menu'),
]
