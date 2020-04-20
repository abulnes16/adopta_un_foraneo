from django.shortcuts import render


def dashboard(request):
    return render(request, 'POST-ARRENDATARIOS-FORANEO.html')


def profile(request):
    return render(request, 'userprofile.html')