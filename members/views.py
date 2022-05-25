from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from social_app.models import Profile


def login_view(request):
    profiles = Profile.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Redirect to a success page.
            login(request, user)
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, "There was an error logging in, try again!")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {"profiles": profiles})


def logout_view(request):
    logout(request)
    return redirect('/')
