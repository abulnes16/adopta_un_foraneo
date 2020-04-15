from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .forms import LoginForm
from apps.users.forms import UserForm, ProfileForm
from apps.users.models import Role
from django.contrib.auth.models import Group


def home(request):
    return render(request, 'index.html')


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('dashboard')
    success_message = ''



    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,'Nombre de usuario o contraseña incorrecta')
        return self.render_to_response(
            self.get_context_data(request=self.request,form=form)
        )


def signup(request):
    context = {'user_form': UserForm, 'profile_form': ProfileForm}
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.password = make_password(user.password)
            profile = profile_form.save(commit=False)
            group_role = Role.objects.get(id=profile.role.id)
            if group_role.description == 'Arrendatario':
                user.is_staff = True
                user.save()
                group = Group.objects.get(name='Arrendador')
                group.user_set.add(user)
            user.save()
            profile.user = user
            profile.save()
            return redirect('login')
        else:
            messages.error(request, 'Uno o mas campos requeridos no fueron enviados, completa los campos requeridos')
            return render(request, 'signup.html', context)

    return render(request, 'signup.html', context)


