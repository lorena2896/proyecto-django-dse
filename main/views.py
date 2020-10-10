from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Producto

def home(request):
    return HttpResponse("Hola Mundo. Te encuentras en la página de inicio de Linio Express")
    
class ProductListView(ListView):
    model = Producto

class ProductDetailView(DetailView):
    model = Producto

