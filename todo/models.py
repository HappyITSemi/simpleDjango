from django.db import models


class TodoCategory(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='カテゴリー名',
    )
    due = models.DateField(
        blank=True,
        verbose_name='期限日',
        null=True,
    )

    class Meta:
        managed = False
        verbose_name_plural = 'TodoCategory'
        db_table = 'todo_category'

    def __str__(self):
        return self.name

    pass


class Todo(models.Model):
    # id = models.AutoField(Primary_key=True)
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
        verbose_name='期限日',
        help_text='期日を入力してください',
        blank=True,
    )
    created_at = models.DateTimeField(
        # auto_now_add=True,
        verbose_name='登録日時',
    )
    updated_at = models.DateTimeField(
        auto_now_add=False,
        verbose_name='更新日時',
        blank=True,
    )
    todo_category_id = models.OneToOneField(TodoCategory, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        verbose_name_plural = 'TodoList'
        db_table = 'todo'

    def __str__(self):
        return self.name
