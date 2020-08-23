from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import GalleryUserCreationForm

# Create your views here.


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
        form = GalleryUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
