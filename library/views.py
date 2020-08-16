from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import *
# Create your views here.

def index(request):
    books_list = Book.objects.order_by('id')[:5]
    context = {'books_list': books_list }
    return render(request, 'library/index.html', context)

#Question.objects.order_by('-pub_date')[:5]
