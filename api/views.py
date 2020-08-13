#
from rest_framework import viewsets, status, generics, filters, mixins
from rest_framework.pagination import PageNumberPagination

from api.serializers import TodoSerializer, TodoCategorySerializer
from todo.models import Todo, TodoCategory


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class TodoListAPIView(generics.ListAPIView):
    model = Todo
    queryset = Todo.objects.order_by('pk')
    serializer_class = TodoSerializer
    pagination_class = StandardResultsSetPagination

    # filter_backends = [filters.DjangoFilterBackend]
    # [HowToUse] - list
    # http://127.0.0.1:8000/api/v1/?page=1&format=json
    # http://127.0.0.1:8000/api/v1/?page=2&format=json
    # [Get id]:http://127.0.0.1:8000/api/v1/{id}
    # [Post, Put, Delete] - See : http://127.0.0.1:8000/api/v1/{id}


class TodoRetrieveAPIView(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.GenericAPIView):
    model = Todo
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TodoCategoryAPIView(generics.ListAPIView):
    queryset = TodoCategory.objects.all()
    serializer_class = TodoCategorySerializer


class TodoCategoryRetrieveAPIView(mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  generics.GenericAPIView):
    model = TodoCategory
    queryset = TodoCategory.objects.order_by('pk')
    serializer_class = TodoCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
