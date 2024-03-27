from cmath import log
from ssl import create_default_context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Item
#views for a given users dashboard

@login_required
def index(request):
    '''get all items listed by a given user'''
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })

