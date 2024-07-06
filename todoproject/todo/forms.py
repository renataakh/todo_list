from django import forms
from .models import todo_list

class TaskForm(forms.ModelForm):
    class Meta:
        model = todo_list
        fields = ['text']
        labels = {
            'text': 'Task description'
        }
        widgets = {
            'text': forms.TextInput(attrs={'size': 50}),
        }

