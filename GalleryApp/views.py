from django.views.generic import ListView
from .models import Photo

# Create your views here.


class PhotoCarouselView(ListView):
    model = Photo
    template_name = 'home.html'
    context_object_name = 'photos'
    paginate_by = 5
    queryset = Photo.objects.all().order_by('id')
