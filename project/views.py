from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    """ Direcciona a portfolio"""
    projects = Project.objects.all()
    return render(request, 'project/portfolio.html',{'projects': projects})