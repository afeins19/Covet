from unicodedata import category
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.db.models import Q  #need this for searchin in different fields (item names, item descriptions etc.)
from item.forms import NewItemForm, EditItemForm
from .models import Item, Category

def items(request):
    '''get all unsold items from db...use in search function'''
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)  #backend for items.html category function...lets links to categories redirect 
    categories = Category.objects.all() 
    items = Item.objects.filter(is_sold=False)
    
    if category_id: 
        items = items.filter(category_id=category_id)

    if query:
        '''Use Q for querrying different search fields '''
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query)) #super weird but we need this to process the querry (use user's search string)

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),    #cast to int to get integer primary key in url
    })

def detail(request, pk):
    '''requires primary key (pk) for a given items model'''
    item = get_object_or_404(Item, pk=pk)

    '''shows n-related items if they exist when on a detail view'''
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', { 
        'item': item,
        'related_items': related_items
    })  #view for the details for a particular item

@login_required #django will require you to login before listing a new item
def new(request):
    '''creating new listings'''
    if request.method=='POST':  #checks if incoming request is a POST from the user
        form = NewItemForm(request.POST, request.FILES)
    
        if form.is_valid():
            item = form.save(commit=False)  #create item object before commiting to the db
            item.created_by = request.user 
            item.save()

            return redirect('item:detail', pk=item.id)
    
    else:   #if incoming request is GET...
        form = NewItemForm()    #otherwise return the default new listing form

    return render(request, 'item/form.html', {
        'form': form,
        'title': "Create Post",
    })

@login_required
def delete(request, pk):    #retrieve primary key to delete seleced item
    '''if user is logged in, make sure only valid items created by the user are 
        able to be deleted
    '''
    item = get_object_or_404(Item, pk=pk, created_by=request.user) #get object by primary key
    item.delete()

    return redirect('dashboard:index')

@login_required #django will require you to login before editing an item
def edit(request, pk):
    '''if user is logged in, make sure only valid items created by the user are 
        able to be edited
    '''
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method=='POST':  #checks if incoming request is a POST from the user
        form = EditItemForm(request.POST, request.FILES, instance=item)
    
        if form.is_valid():
            item = form.save(commit=False)  #create item object before commiting to the db
            item.created_by = request.user 
            item.save()

            return redirect('item:detail', pk=item.id)
    
    else:   #if incoming request is GET...
        form = EditItemForm(instance=item)    #otherwise return the default edit form

    return render(request, 'item/form.html', {
        'form': form,
        'title': "Edit Listing",
    })
