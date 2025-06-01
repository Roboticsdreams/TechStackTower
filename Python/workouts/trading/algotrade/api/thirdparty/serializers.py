from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['token', 'symbol', 'stock_name', 'exchange', 'deleted_at']
        read_only_fields = ['deleted_at']  # Prevents updating the soft-delete field directly
