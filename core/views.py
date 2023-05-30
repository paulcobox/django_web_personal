from django.shortcuts import render

# Create your views here.
def home(request):
    """ Direcciona a home"""
    return render(request, 'core/home.html')

def about_us(request):
    """ Direcciona a about_us"""
    return render(request, 'core/about_us.html')

def contact(request):
    """ Direcciona a contact"""
    return render(request, 'core/contact.html')


