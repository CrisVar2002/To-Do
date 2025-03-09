# taskmanager/urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home(request):
    return redirect('task_list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('', home),
]