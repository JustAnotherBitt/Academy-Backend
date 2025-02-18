from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from .api import api

# Automatically redirects to /api/docs when accessing the site root
def redirect_to_docs(request):
    return HttpResponseRedirect('/api/docs')

urlpatterns = [
    path('', redirect_to_docs),  # Redirect root to /api/docs
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
