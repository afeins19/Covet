
from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    #front page shows some items...passing in the objects here 
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    }) 

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def legal(request):
    return render(request, 'core/legal.html')

def about(request):
    return render(request, 'core/about.html')

def terms(request):
    return render(request, 'core/terms.html')

def signup(request):
    '''First, check if POST has been made...form has been submited'''
    if request.method == 'POST':
        form = SignupForm(request.POST) #retrieve filled out form

        if form.is_valid():
            form.save() #save valid form to db

            return redirect('/login/')

    else: #if request is GET...
        form = SignupForm() #set an empty sign up form

    return render(request, 'core/signup.html', {
        'form': form
    }) 