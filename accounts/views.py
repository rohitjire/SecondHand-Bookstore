from django.shortcuts import render, redirect
from core.models import User
from django.contrib import messages
from django.core.mail import send_mail
import random
import string


def randomString(stringlength=6):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringlength))


code = randomString()


# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']
        user = User

        context = {

            first_name: 'first_name',
            last_name: 'last_name',
            username: 'username',
            email: 'email',
            phone: 'phone',
            password: 'password',
            password2: 'password2',

        }

        if password == password2:
            if user.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken!')
                return redirect('register')
            else:
                if user.objects.filter(email=email).exists():
                    messages.error(request, 'Email Id is already exists!')
                    return redirect('register')
                else:
                    if user.objects.filter(phone=phone).exists():
                        messages.error(request, 'Phone number is already exists!')
                        return redirect('register')
                    else:
                        send_mail(
                            'Account Creation Confirmation',
                            'Hi' + first_name + 'Your Confirmation code is: ' + code,
                            [email],
                            fail_silently=False
                        )
                        request.method = 'GET'
                        return render(request, 'accounts/confirmregister.html', context)
        else:
            messages.error(request, 'Password do not match!')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')
