from django.shortcuts import render

import random
import string


def randomString(stringlength=6):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringlength))


code = randomString()


# Create your views here.

def register(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'accounts/register.html')
