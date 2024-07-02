from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.contrib import messages


class GroupRequiredMixin(AccessMixin):
    """
    Mixin to check if the authenticated user belongs to a specific group.
    """

    group_required = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # return self.handle_no_permission()
            return redirect("/")

        user_group = request.user.groups.values_list("name", flat=True)
        if self.group_required in user_group:
            print(list(user_group))
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request, "You are not allowed to view this page.")
            return redirect("/")
