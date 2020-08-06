from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from todo.forms import TodoForm
from todo.models import Todo


# *args: 複数の引数をタプルとして受け取る
# **kwargs: 複数のキーワード引数を辞書として受け取る


class TodoIndexView(generic.TemplateView):
    template_name = "index.html"  # テンプレート名のデフォルトは モデル名_index.html が使われる


class TodoListView(ListView):  # テンプレート名のデフォルトは モデル名_list.html が使われる
    template_name = "list.html"
    model = Todo
    paginate_by = 10
    queryset = Todo.objects.order_by('pk')


class TodoDetailView(DetailView):
    template_name = "detail.html"
    model = Todo


class TodoCreateView(CreateView):
    model = Todo

    form_class = TodoForm
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, '「{}」を作成しました'.format(form.instance))
        return result


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm

    success_url = reverse_lazy('list')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を更新しました'.format(form.instance))
        return result


class TodoDeleteView(DeleteView):
    model = Todo
    form_class = TodoForm

    success_url = reverse_lazy('list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(self.request, '「{}」を削除しました'.format(self.object))
        return result
