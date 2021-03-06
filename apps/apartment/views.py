from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from apps.users.models import Profile
from django.contrib import messages
from apps.users.forms import UpdateProfileForm
from .models import Apartment, Comments


def dashboard(request):
    apartments = Apartment.objects.all()
    context = {'apartments': apartments}
    return render(request, 'POST-ARRENDATARIOS-FORANEO.html', context)


def apartment_detail(request, id):
    apartment = get_object_or_404(Apartment, id=id)
    comments = Comments.objects.filter(apartment__id=id)
    context = {'apartment': apartment, 'comments': comments}
    return render(request, 'apartment_detail.html', context)


def add_coment(request, id):
    if request.method == 'POST':
        user = request.user.profile
        content = request.POST['contenido']
        Comments.objects.create(user=user, apartment_id=id, content=content)
    return redirect('details', id=id)


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
