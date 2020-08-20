from django.views.generic import TemplateView, CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import GalleryUserCreationForm

# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"


def sign_up(request):
    if request.method == 'POST':
        form = GalleryUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(
                username=username,
                password=raw_password
            )
            login(request, user)
            return redirect('home')
        else:
            print('form error: ' + form.errors.__str__())
    else:
        form = GalleryUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
