from django.http import HttpResponse
from django.urls import path

from api import views


def api_test(request):
    return HttpResponse("api_test")


app_name = 'api'
urlpatterns = [
    path('', api_test),
    path('v1/', views.TodoListAPIView.as_view(), name='list'),
    path('v1/<int:pk>', views.TodoRetrieveAPIView.as_view()),
    path('v1/category/', views.TodoCategoryAPIView.as_view(), name='category_list'),
    path('v1/category/<int:pk>', views.TodoCategoryRetrieveAPIView.as_view()),
]
