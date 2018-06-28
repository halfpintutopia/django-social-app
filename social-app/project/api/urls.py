from django.urls import path

# from project.feed.views import MyView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import logout
# from django.views.generic import RedirectView

from project.api.views.overview import OverviewView

app_name = 'api'

urlpatterns = [
    # path('', MyView.as_view(), name='index')
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', view=logout, name='logout'),
    # path('logout/', RedirectView.as_view(url='/')),
    path('', OverviewView.as_view(), name='overview'),
]
