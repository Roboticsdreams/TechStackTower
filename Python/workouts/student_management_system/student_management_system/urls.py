# student_management_system/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.students.urls')),  # Include students app urls
    path('api/', include('apps.courses.urls')),  # Include courses app urls
]
