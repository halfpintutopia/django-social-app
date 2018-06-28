from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from project.feed.models import Post


class OverviewView(LoginRequiredMixin, TemplateView):
    template_name = 'overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-created')
        return context