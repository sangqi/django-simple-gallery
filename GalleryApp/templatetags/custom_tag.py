from django import template
from django.urls import NoReverseMatch, reverse
from GalleryApp.models import GalleryUser, Photo, Like

register = template.Library()


@register.simple_tag
def has_user_liked_photo(photo, user):
    try:
        like = Like.objects.get(photo=photo, user=user)
        return True
    except:
        return False
