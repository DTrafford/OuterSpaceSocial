from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from . import forms
# Create your views here.
class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    # REVERSE LAZY WAITS UNTIL THEY ACTUALLY HIT SUBMIT
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
