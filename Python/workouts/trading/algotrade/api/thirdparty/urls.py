# urls.py
from django.urls import path
from .views import (MyModelViewSet)

urlpatterns = [
    path('third-party/', MyModelViewSet.as_view({'get': 'list', 'post': 'sync'}), name='third-party'),
]