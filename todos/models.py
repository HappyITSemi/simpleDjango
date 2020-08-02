from django.db import models


# Create your models here.
# from django.db.models import AutoField, CharField, DateField

class TodoList(models.Model):
    # todolist_id = models.AutoField(Primary_key=True)
    name = models.CharField(
        max_length=64,
        verbose_name='Todoタイトル名',
        help_text='Todoタイトルを入力してください',
    )
    description = models.CharField(
        max_length=128,
        verbose_name='内容',
        help_text='Todo内容を入力してください',
    )
    due_date = models.DateField(
        auto_now_add=True,
        verbose_name='期限日',
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='登録日時',
    )
    updated_at = models.DateTimeField(
        auto_now_add=False,
        verbose_name='更新日時',
        blank=True,
    )

    class Meta:
        verbose_name_plural = 'Todo'

    def __str__(self):
        return self.name
