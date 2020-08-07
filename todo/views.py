from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from todo.forms import TodoForm
from todo.models import Todo, TodoCategory


# *args: 複数の引数をタプルとして受け取る
# **kwargs: 複数のキーワード引数を辞書として受け取る


class TodoIndexView(generic.TemplateView):
    template_name = "index.html"  # テンプレート名のデフォルトは モデル名_index.html が使われる

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す
        context["greeting"] = "Hi, Morning"

        todo_category = TodoCategory.objects.values('id', 'name')
        context['categories'] = todo_category

        return context


class TodoListView(ListView):  # テンプレート名のデフォルトは モデル名_list.html が使われる
    model = Todo
    template_name = "list.html"

    paginate_by = 10
    queryset = Todo.objects.order_by('pk')


class TodoDetailView(DetailView):
    model = Todo
    template_name = "detail.html"


class TodoCreateView(CreateView):
    model = Todo
    template_name = "create.html"
    form_class = TodoForm
    success_url = reverse_lazy('todo:list')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, '「{}」を作成しました'.format(form.instance))
        return result

    def form_invalid(self, form):
        messages.warning(self.request, "保存できませんでした")
        return super().form_invalid(form)


class TodoUpdateView(UpdateView):
    model = Todo
    template_name = "update.html"
    form_class = TodoForm
    success_url = reverse_lazy('todo:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す
        todo_category = TodoCategory.objects.values('id', 'name')
        context['categories'] = todo_category
        return context

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, '「{}」を更新しました'.format(form.instance))
        return result

    def form_invalid(self, form):
        messages.warning(self.request, "保存できませんでした")
        return super().form_invalid(form)


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "delete.html"
    form_class = TodoForm
    success_url = reverse_lazy('todo:list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(self.request, '「{}」を削除しました'.format(self.object))
        return result
