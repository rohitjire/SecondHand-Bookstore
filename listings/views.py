from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage


# Create your views here.

def listings(request):
    return render(request, 'listings/listings.html')


def listing(request, pk):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
