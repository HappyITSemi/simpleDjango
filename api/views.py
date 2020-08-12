#
from rest_framework import viewsets, status, generics, filters
from rest_framework.response import Response

from api.serializers import TodoSerializer, TodoCategorySerializer
from todo.models import Todo, TodoCategory


class TodoListAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    #    filter_backends = [filters.DjangoFilterBackend]

    def get(self, *args, **kwargs):
        todo_list = Todo.objects.all()
        serializer = TodoSerializer(instance=todo_list, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class TodoCategoryViewSet(viewsets.ModelViewSet):
    queryset = TodoCategory.objects.all()
    serializer_class = TodoCategorySerializer
