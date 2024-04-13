from django.urls import path

from .views import Login, Trader

urlpatterns = [
    path('', Login.as_view()),
    path('trdr', Trader.as_view()),
]