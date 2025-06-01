from rest_framework import serializers
from .models import MasterTable

class MasterTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterTable
        fields = '__all__'
        extra_kwargs = {
            'constant_name': {'required': False},
            'stock_table': {'required': False},
            'option_table': {'required': False}
        }

        def validate(self, data):
            if not data['constant_name']:
                data['constant_name'] = f"CONSTANT_{data['stock_name']}".upper()
            constant_name = data['constant_name']
            data['stock_table'] = f"STOCK_{constant_name}".upper()
            data['option_table'] = f"OPTION_{constant_name}".upper()
            return data

class DynamicTableSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()