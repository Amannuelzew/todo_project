from typing import Any
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView,FormView
from django.views.generic import ListView,View
from .forms import TodoForm
from .models import Todo


# Create your views here.


class IndexView(View):
    def get(self,request):
        form=TodoForm()
        todos=Todo.objects.all().order_by("-date")
        return render(request,"todo/index.html",{"form":form,"todo":todos})
    def post(self,request):
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        return render(request,"todo/index.html",{"form":form})
    
    def get_context_data(self, **kwargs: Any) :
        context= super().get_context_data(**kwargs)
        todos=Todo.objects.all().order_by("-date")
        print("heloooopppppppp")
        context['todos']=todos
        context['text']="miss yhs"
        return context


def index(request):
    if request.method=="POST":
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            a=Todo.objects.all()
            print(a.count())
            return HttpResponseRedirect("/")
        return render(request,"todo/index.html",{"form":form})
    form=TodoForm()
    todos=Todo.objects.all().order_by("-date")
    return render(request,"todo/index.html",{"form":form,"todos":todos})