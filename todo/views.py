from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView,FormView
from .forms import TodoForm
from .models import Todo


# Create your views here.

class IndexView(FormView):
    template_name="todo/index.html"
    form_class=TodoForm
    success_url="/"

    def form_valid(self, form) :
        form.save()
        return super().form_valid(form)