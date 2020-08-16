from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .models import *



def index(request):
    menu_list = Menu.objects.order_by('id')
    menu_type_list = MenuType.objects.order_by('id')
    context = {
    'menu_list': menu_list,
    'menu_type_list':menu_type_list,
     }
    return render(request, 'restaurant/index.html', context)

def breakfast(request):
    menu_list = Menu.objects.filter(type=1)
    print(menu_list)
    context = {
    'menu_list': menu_list, }

    return render(request, 'restaurant/breakfast.html', context)
