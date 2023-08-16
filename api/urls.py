from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, Event_api_admin, Event_api

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),

    path('admin', Event_api_admin.as_view()),
    path('filter/<str:pk>/<str:b>/', Event_api.as_view(), name= "For Generating Certificate"),
]