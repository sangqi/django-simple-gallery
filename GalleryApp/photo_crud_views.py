from django.views.generic import DeleteView, DetailView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import PhotoCreationForm
from .models import Photo

# Create your views here.


def create_photo(request):
    if request.method == 'POST':
        form = PhotoCreationForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = Photo(
                author=request.user,
                title=form.cleaned_data['title'],
                image=form.cleaned_data['file']
            )
            new_photo.save()
            return redirect('home')
    else:
        form = PhotoCreationForm()
    return render(request, 'photo_create.html', {'form': form})


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo_detail.html'


class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['title']
    template_name = 'photo_update.html'

    def get_success_url(self):
        photoId = self.kwargs['pk']
        return reverse_lazy('photo_detail', kwargs={'pk': photoId})


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = reverse_lazy('home')
