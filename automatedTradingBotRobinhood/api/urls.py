from django.urls import path
from .views import ModelView, BotView

urlpatterns = [
    path('', ModelView.as_view()),
    path('', BotView.as_view())
]