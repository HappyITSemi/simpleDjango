from django.db import models


class TodoCategory(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='カテゴリー名',
    )

    class Meta:
        managed = False
        verbose_name_plural = 'TodoCategory'
        db_table = 'todo_category'

    def __str__(self):
        return self.name


# For DateField: default=date.today - from datetime.date.today()
# For DateTimeField: default=timezone.now - from django.utils.timezone.now()


class Todo(models.Model):
    # id = models.AutoField(Primary_key=True)
    name = models.CharField(
        max_length=64,
    )
    description = models.CharField(
        max_length=128,
        blank=True,
    )
    due_date = models.DateField(
        blank=True,
        verbose_name='期日',
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name='登録日時',
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='更新日時',
    )
    todo_category_id = models.ForeignKey('TodoCategory', models.DO_NOTHING, db_column='todo_category_id ', blank=True,
                                         null=True)

    class Meta:
        managed = False  # 管理対象外とする
        verbose_name_plural = 'Todo'
        db_table = 'todo'

    def __str__(self):
        return self.name

