from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PhotoCarouselView
from .registration_views import sign_up
from .photo_crud_views import create_photo, PhotoDeleteView, PhotoDetailView, PhotoUpdateView
from .ajax_views import toggle_like

urlpatterns = [
    path('', PhotoCarouselView.as_view(), name='home'),
    path('signup/', sign_up, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('photo/create/', create_photo, name='photo_create'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('photo/like/', toggle_like, name='photo_like'),
]
