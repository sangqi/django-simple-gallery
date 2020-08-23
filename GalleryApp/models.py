from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField

# Create your models here.


class GalleryUser(AbstractUser):
    first_name = None
    last_name = None


class Photo(models.Model):
    author = models.ForeignKey(
        GalleryUser,
        on_delete=models.CASCADE,
        related_name='photos'
    )
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='photo',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )
    uploaded_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo_detail', args=[str(self.id)])

    def get_like_count(self):
        return self.likes.count()

    def is_liked_by(self, user):
        return self.likes.filter(user = user).exists()


class Like(models.Model):
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    user = models.ForeignKey(
        GalleryUser,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    class Meta:
        unique_together = ['photo', 'user']

    def __str__(self):
        return 'Like: ' + self.user.username + ' liked ' + self.photo.title
