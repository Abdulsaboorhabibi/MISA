from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin
from django.urls import reverse_lazy


class RedirectAuthenticatedUserMinin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/accounts/")
        return super().dispatch(request, *args, **kwargs)
