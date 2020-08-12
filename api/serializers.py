from rest_framework import serializers

from todo.models import Todo, TodoCategory


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['name', 'description', 'due_date', 'todo_category_id']


class TodoCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoCategory
        fields = ['name']
