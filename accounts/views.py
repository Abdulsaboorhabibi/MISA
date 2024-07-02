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

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            remember_me = request.POST.get("remember_me")
            if remember_me:
                # Set session expiry for "Remember me"
                settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
                settings.SESSION_COOKIE_AGE = settings.REMEMBER_ME_SESSION_COOKIE_AGE
            else:
                # Reset session expiry to default
                settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
                settings.SESSION_COOKIE_AGE = settings.DEFAULT_SESSION_COOKIE_AGE

        return super().dispatch(request, *args, **kwargs)
