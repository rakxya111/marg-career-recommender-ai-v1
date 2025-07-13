from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .forms import CustomUserCreationForm , CustomLoginForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'marg/Account/signup.html'
    success_url = reverse_lazy('login')

class CustomLoginView(auth_views.LoginView):
    template_name = 'marg/Account/login.html'
    authentication_form = CustomLoginForm

    def get_success_url(self):
        return '/'  

@login_required
def custom_logout_view(request):
    logout(request)
    return redirect('/')
