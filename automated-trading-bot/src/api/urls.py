from django.urls import path
from .views import Login
urlpatterns = [
    path('api/login', Login.as_view()),
]