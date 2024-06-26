from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserAuthenthicationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "JhonDoe", "id": "floatingInput"}
        )
        self.fields["password"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Enter your password",
                "id": "floatingPassword",
            }
        )
