# api/backdata/urls.py
from django.urls import path
from .views import (
    MasterTableView,
    DynamicTableListCreateView, 
    DynamicTableDetailView,
    SyncMasterTableView
)

urlpatterns = [
    path('master-tables/', MasterTableView.as_view(), name='master-table-list-create'),
    path('master-tables/<int:pk>/', MasterTableView.as_view(), name='master-table-detail'),
    path('dynamic-tables/<str:table_name>/', DynamicTableListCreateView.as_view(), name='dynamic-table-list-create'),
    path('dynamic-tables/<str:table_name>/<int:pk>/', DynamicTableDetailView.as_view(), name='dynamic-table-detail'),
    path('sync-master-table/', SyncMasterTableView.as_view(), name='sync-master-table'),
]