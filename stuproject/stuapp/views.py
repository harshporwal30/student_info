from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from .models import student
from .forms import stuform
from django.urls import reverse_lazy
# Create your views here.

    
class createview(CreateView):
    model = student
    form_class = stuform
    template_name = "studentform.html"
    success_url = reverse_lazy('show')

class show(ListView):
    model = student
    template_name = "index.html"
    context_object_name = "stu"

class update(UpdateView):
    model=student
    template_name="update.html"
    form_class=stuform
    success_url=reverse_lazy("show")               

class delete(DeleteView):
    model=student
    template_name="confirm_delete.html"
    success_url=reverse_lazy("show")
