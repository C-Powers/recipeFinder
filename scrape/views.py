from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import webbrowser as wb
from .getRecipe import get_Recipe
# Create your views here.

def baseSite(request):
    return render(request, 'scrape/base.html', {})

def newSite(request):
    # link = "https://www.google.com/"
    # wb.open(link)
    redirectUrl = get_Recipe()
    return redirect(redirectUrl)
