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
        error_messages={
            "title":{"required":"a"},
            "is_completed":{"required":"b"},
            "date":{"required":"c"}
        }
