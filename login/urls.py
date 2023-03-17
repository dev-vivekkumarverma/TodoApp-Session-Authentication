from django.urls import path,include
from .views import AuthenticationView,LoginView
urlpatterns = [
    path('',AuthenticationView.as_view()),
    path('login/',LoginView.as_view()),
]
