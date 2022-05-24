from django.shortcuts import render
from .models import Profile


def dashboard(request):
    return render(request, "social_app/pages/base.html")


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "social_app/partials/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(request, "social_app/partials/profile.html", {"profile": profile})
