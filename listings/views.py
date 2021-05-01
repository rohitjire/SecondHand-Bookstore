from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage


# Create your views here.

def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {
        'listings': page_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
