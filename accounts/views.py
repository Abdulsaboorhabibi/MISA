from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.forms import UserAuthenthicationForm


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/profile.html"


class UserLoginView(LoginView):
    user_redirected_url = True
    authentication_form = UserAuthenthicationForm
    template_name = "accounts/login.html"
    success_url = reverse_lazy("accounts/profile/")
