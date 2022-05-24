from django.shortcuts import render
from .models import Profile


def dashboard(request):
    return render(request, "social_app/pages/base.html")


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "social_app/partials/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)

    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")

        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)

        current_user_profile.save()
    return render(request, "social_app/partials/profile.html", {"profile": profile})
