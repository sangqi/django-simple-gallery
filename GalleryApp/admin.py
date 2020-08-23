from django.contrib import admin
from GalleryApp.models import GalleryUser, Photo, Like

# Register your models here.
admin.site.register(GalleryUser)
admin.site.register(Photo)
admin.site.register(Like)
