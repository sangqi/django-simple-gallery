from annoying.decorators import ajax_request
from .models import Photo, Like


@ajax_request
def toggle_like(request):
    photo_pk = request.POST.get('photo_pk')
    photo = Photo.objects.get(id=photo_pk)
    try:
        like = Like(photo=photo, user=request.user)
        like.save()
        liked = True
    except Exception as e:
        like = Like.objects.get(photo=photo, user=request.user)
        like.delete()
        liked = False

    like_count = Like.objects.filter(photo=photo).count()
    return {
        'liked': liked,
        'like_count': like_count,
        'photo_pk': photo_pk
    }
