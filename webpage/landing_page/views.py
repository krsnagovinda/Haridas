from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView


# vistas de pagina web

def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def services(request):
    return render(request, 'services_details.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')