from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts import views

urlpatterns = [
    path("", views.ProfileView.as_view(), name="profile"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="/accounts/login/"), name="logout"),
]
