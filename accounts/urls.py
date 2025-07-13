from django.urls import path
from .views import RegisterView, CustomLoginView  # import your custom login view
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from accounts import views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout_view, name='logout'),

]
