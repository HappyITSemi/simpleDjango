from django.contrib import admin

from todo.models import Todo, TodoCategory

admin.site.register(Todo)
admin.site.register(TodoCategory)
