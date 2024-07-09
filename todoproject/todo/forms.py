from django import forms
from .models import TodoList


class TaskForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = ['text']
        labels = {
            'text': 'Task description'
        }
        widgets = {
            'text': forms.TextInput(attrs={'size': 50}),
        }
