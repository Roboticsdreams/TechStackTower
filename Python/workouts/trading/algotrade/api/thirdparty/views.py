# api/thirdparty/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
import requests
from .models import MyModel
from .serializers import MyModelSerializer
import logging

logger = logging.getLogger(__name__)

class MyModelViewSet(viewsets.ViewSet):
    
    # GET request to fetch all active records (not soft deleted)
    def list(self, request):
        queryset = MyModel.objects.filter(deleted_at__isnull=True)  # Exclude soft-deleted records
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)
    
    # POST request to sync data from the URL
    @action(detail=False, methods=['post'])
    def sync(self, request):
        url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Ensure the request was successful
            data = response.json()  # Assuming the response is JSON

            # Store all incoming external_ids to track what's present in the new data
            incoming_ids = set()

            # Update existing records or create new ones
            for item in data:
                logger.info(item)
                token = item['token']
                incoming_ids.add(token)
                
                # Update or create record using the serializer
                obj, created = MyModel.objects.update_or_create(
                    token=token,
                    defaults={
                        'stock_name': item.get('name'),
                        'symbol': item.get('symbol'),
                        'exchange': item.get('exch_seg'),
                        'deleted_at': None  # Restore if previously soft-deleted
                    }
                )

            # Mark rows not present in the new data as soft-deleted
            MyModel.objects.filter(deleted_at__isnull=True).exclude(external_id__in=incoming_ids).update(deleted_at=timezone.now())

            return Response({'status': 'success', 'message': 'Data synchronized successfully.'})

        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
