from django.shortcuts import render, redirect
import webbrowser as wb
from .getRecipe import get_Recipe
# Create your views here.

def baseSite(request):
    return render(request, 'scrape/base.html', {})

def newSite(request):
    # link = "https://www.google.com/"
    # wb.open(link)
    get_Recipe()
    return redirect('http://127.0.0.1:8000/')
