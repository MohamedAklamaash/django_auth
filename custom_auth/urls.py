from rest_framework.urls import path
from .views import SignupUser

urlpatterns = [
    path("signup",SignupUser.as_view(),name="signup-user")
]