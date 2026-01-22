from django.urls import path
from .views import flashcard_view

urlpatterns = [
    path('', flashcard_view, name='flashcard'),
]
