from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'status': 'Estado',
        }