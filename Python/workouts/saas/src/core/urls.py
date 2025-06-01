from django.contrib import admin
from django.urls import path, include
from core.views import index, home_view, inline_view, template_view, inheritance_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('home/', home_view, name='home'),
    path('inline/', inline_view, name='inline'),
    path('template/', template_view, name='template'),
    path('inheritance/', inheritance_view, name='inheritance'),
    path('visits/', include('visits.urls')),
]
