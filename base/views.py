from django.shortcuts import render
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
    TemplateView,
)


# Base view of the application.
class IndexView(TemplateView):
    template_name = "base/index.html"


class AboutView(TemplateView):
    template_name = "base/about.html"


class ContactView(TemplateView):
    template_name = "base/index.html"
