from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, HelloWorldView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('test', HelloWorldView.as_view()),
]