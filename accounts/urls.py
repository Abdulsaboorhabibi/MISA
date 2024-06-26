from django.urls import path
from accounts import views

urlpatterns = [
    path("", views.ProfileView.as_view(), name="profile"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogout.as_view(), name="logout"),
]
