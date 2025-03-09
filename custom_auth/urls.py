from rest_framework.urls import path
from .views import SignupUser,SigninView

urlpatterns = [
    path("signup",SignupUser.as_view(),name="signup-user"),
    path("signin",SigninView.as_view(),name="signin-view")
]