from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegistrationForm
from django.contrib.auth import get_user_model



class RegisterUser(CreateView):
    model = get_user_model()
    form_class = UserRegistrationForm
    template_name ='registration.html'
    success_url= reverse_lazy('login')