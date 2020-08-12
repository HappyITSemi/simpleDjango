# 検索で使う入力項目はFormを、
# 登録・更新で使う入力項目はModelFormを利用する
#

from django import forms
from .models import Todo, TodoCategory


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'description', 'due_date', 'todo_category_id']


# widgetsで各フィールドのデザインを指定する

class TodoCategory(forms.ModelForm):
    class Meta:
        model = TodoCategory
        fields = ['name']
