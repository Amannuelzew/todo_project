from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        exclude=["date","is_completed"]
        labels={
            "title":""
        }
        widgets={
            "title":forms.TextInput(attrs={'placeholder':"Todo"})
        }
