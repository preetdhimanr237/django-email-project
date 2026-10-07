from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_mail(
                'Welcome to the Email Project',
                f"Hello {user.first_name}, you are registered Successfully ",
                settings.EMAIL_SENDER,
                [user.email],
                fail_silently=False,
            )

            return redirect('home')

    form = RegisterForm()
    return render(request,'register.html',{'form':form})    


def home(requets):
    return  HttpResponse("Welcome to the page")