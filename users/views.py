# users/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm  # Import your custom form


def users(request):
    template = loader.get_template('users.html')
    return HttpResponse(template.render({}, request))


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
