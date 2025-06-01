# utils.py
from django.db import models, connection
from .models import AuditTable

def create_dynamic_model(table_name):
    class Meta:
        db_table = table_name
        app_label = 'api.backdata'
    
    attrs = {
        '__module__': 'api.backdata.models',
        'Meta': Meta,
        'id': models.AutoField(primary_key=True), # Ensure id is primary key and auto-incremented
        'title': models.CharField(max_length=255),
        'description': models.TextField(),
    }
    
    return type(table_name, (models.Model,), attrs)

def create_table_if_not_exists(table_name):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(255),
                description TEXT
            )
        """)
        print(f"Created table {table_name}")

def delete_table_if_exists(table_name):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            DROP TABLE IF EXISTS {table_name}
        """)
        print(f"Deleted table {table_name}")

def create_delete_dynamic_table(data):
    if data.get('is_stock_active') == True:
        create_table_if_not_exists(data.get('stock_table'))
    if data.get('is_option_active') == True:
        create_table_if_not_exists(data.get('option_table'))
    if data.get('is_stock_active') == False:
        delete_table_if_exists(data.get('stock_table'))
    if data.get('is_option_active') == False:
        delete_table_if_exists(data.get('option_table'))

def delete_dynamic_table(data):
    if data.get('stock_table'):
        delete_table_if_exists(data.get('stock_table'))
    if data.get('option_table'):
        delete_table_if_exists(data.get('option_table'))

def updated_audit_fields(master, serializer):
    for field, new_value in serializer.validated_data.items():
        old_value = getattr(master, field)
        if old_value != new_value:
            AuditTable.objects.create(
                master_table=master,
                field_name=field,
                old_value=old_value,
                new_value=new_value,
            )  
    