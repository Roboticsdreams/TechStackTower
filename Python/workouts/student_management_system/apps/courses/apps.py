# apps/courses/apps.py

from django.apps import AppConfig

class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.courses'  # Ensure this points to the correct module path
