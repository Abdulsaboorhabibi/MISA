from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from accounts.forms import UserAuthenthicationForm
from accounts.account_mixins import RedirectAuthenticatedUserMinin


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/profile.html"


class UserLoginView(RedirectAuthenticatedUserMinin, LoginView):
    user_redirected_url = True
    authentication_form = UserAuthenthicationForm
    template_name = "accounts/login.html"
    success_url = reverse_lazy("accounts/profile/")
