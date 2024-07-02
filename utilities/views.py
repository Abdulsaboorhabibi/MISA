from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .group_required_mixin import GroupRequiredMixin
from utilities.models import Location


class LocationList(GroupRequiredMixin, ListView):
    group_required = "Location"
    model = Location
