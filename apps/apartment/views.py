from django.shortcuts import render


def dashboard(request):
    return render(request, 'userhome.html')


def profile(request):
    return render(request, 'userprofile.html')