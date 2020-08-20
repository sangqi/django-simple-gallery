from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeView, sign_up, logout

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', sign_up, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
