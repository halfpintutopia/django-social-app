from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView

from .models import ExampleModel


class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World!')


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_example'] = ExampleModel.objects.all()[:5]
        return context
