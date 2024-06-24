from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/profile.html"


class UserLoginView(LoginView):
    user_redirected_url = True
    template_name = "accounts/login.html"
    success_url = reverse_lazy("accounts/profile/")
