from django.urls import path
from . import views
from .views import SignUpView


urlpatterns = [
    path('users/', views.users, name='users'),
    path("signup/", SignUpView.as_view(), name="signup"),
]
