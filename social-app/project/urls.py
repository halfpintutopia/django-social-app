from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # This is the new urls we include now
    # path('/', include('example_app.urls')),

    # Already existing urls
    path('backend/admin/', admin.site.urls),
    path('backend/api/', include('project.api.urls', namespace='api')),

]
