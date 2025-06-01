from django.urls import path
from .views import pagevisit_view

urlpatterns = [
    path('pagevisit/', pagevisit_view, name='pagevisit'),
]