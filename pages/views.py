from django.shortcuts import render
from listings.choices import branch_choices, semester_choices, category_choices
from listings.models import Listing


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'branch_choices': branch_choices,
        'category_choices': category_choices,
        'semester_choices': semester_choices,
    }
    return render(request, 'pages/index.html',context)


def about(request):
    return render(request, 'pages/about.html')
