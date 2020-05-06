from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from apps.users.models import Profile
from django.contrib import messages
from apps.users.forms import UpdateProfileForm


def dashboard(request):
    return render(request, 'POST-ARRENDATARIOS-FORANEO.html')


def profile(request):
    current_user = request.user
    current_profile = get_object_or_404(Profile, user=current_user)
    profile_form = UpdateProfileForm(instance=current_profile)
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=current_profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'El perfil se actualizó con éxito')
            return redirect(reverse_lazy('profile'))
        else:
            messages.info(request, 'Los datos no se actualizaron')
    context = {'profile_form': profile_form, 'profile': current_profile}

    return render(request, 'userprofile.html', context)

