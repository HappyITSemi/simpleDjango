from django.views.generic import TemplateView


# *args: 複数の引数をタプルとして受け取る
# **kwargs: 複数のキーワード引数を辞書として受け取る
#
class TodoIndexView(TemplateView):
    template_name = "index.html"


class PostMenuView(TemplateView):
    template_name = "input_menu.html"
