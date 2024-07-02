from django.urls import path
from utilities.views import LocationList

urlpatterns = [
    path("locations/", LocationList.as_view(), name="locations"),
]
