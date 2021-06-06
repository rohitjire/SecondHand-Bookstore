from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Inquiry
from django.core.mail import send_mail


# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        owner_mail = request.POST['owner_mail']
        owner_id = request.POST['owner_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_inquired = Inquiry.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_inquired:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)
            inquiry = Inquiry(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone,
                              message=message, user_id=user_id,owner_id=owner_id)
            inquiry.save()
            send_mail(
                'Inquiry for' + listing,
                'There has been a inquiry for' + listing + '.Sign in to you dashboard for further info',
                'rohitjire55@gmail.com',
                [owner_mail],
                fail_silently=False
            )
            messages.success(request, 'Your inquiry has been made, the Owner of the post will get back to you asap')
            return redirect('/listings/' + listing_id)