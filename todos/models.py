from django.db import models

# Create your models here.
from django.db.models import AutoField, CharField, DateField


class TodosTbl(models.Model):
    todo_id = models.AutoField(Primary_key=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    due_date = models.DateField()
