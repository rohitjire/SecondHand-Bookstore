from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ListingForm, UpdateForm
from .models import Listing
from django.core.paginator import Paginator, EmptyPage
from .choices import  branch_choices, semester_choices, category_choices


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
    query_set = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set = query_set.filter(title__icontains=keywords)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_set = query_set.filter(city__iexact=city)
    if 'branch' in request.GET:
        branch = request.GET['branch']
        if branch:
            query_set = query_set.filter(branch__iexact=branch)
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            query_set = query_set.filter(category__iexact=category)
    if 'semester' in request.GET:
        semester = request.GET['semester']
        if semester:
            query_set = query_set.filter(semester__iexact=semester)

    context = {
        'query_set': query_set,
        'branch_choices': branch_choices,
        'category_choices': category_choices,
        'semester_choices': semester_choices,
        'values': request.GET,
    }

    return render(request, 'listings/search.html', context)


@login_required
def create(request):
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.owner = request.user
            new.save()
            return redirect('dashboard')
        else:
            pass
    else:
        return render(request, 'listings/create.html', {'form': ListingForm()})


@login_required
def update(request, pk):
    listing = get_object_or_404(Listing, pk=pk, owner=request.user)
    context = {
        'form': UpdateForm(instance=listing),
        'update': True,
        'pk': pk
    }
    if request.method == "POST":
        form = UpdateForm(request.POST, request.FILES, instance=listing)
        print(form)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        return render(request, 'listings/create.html', context)


@login_required
def delete_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk, owner=request.user)
    if request.method == "POST":
        listing.delete()
        return redirect('dashboard')
