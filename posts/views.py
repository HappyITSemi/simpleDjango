#
#
from django.views.generic import TemplateView


class PostIndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 処理
        return context
