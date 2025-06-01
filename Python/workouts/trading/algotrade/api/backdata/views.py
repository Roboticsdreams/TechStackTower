# api/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MasterTable
from .serializers import MasterTableSerializer, DynamicTableSerializer
from .utils import create_dynamic_model, create_table_if_not_exists, updated_audit_fields, create_delete_dynamic_table, delete_dynamic_table
from django.shortcuts import get_object_or_404
import ijson
import json
import requests
import logging

logger = logging.getLogger(__name__)

class MasterTableView(APIView):
    def get(self, request, pk=None):
        if pk:
            instance = get_object_or_404(MasterTable, pk=pk)
            serializer = MasterTableSerializer(instance)
        else:
            queryset = MasterTable.objects.all()
            serializer = MasterTableSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MasterTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            create_delete_dynamic_table(serializer.data)
            logger.info(f"Created MasterTable with ID {serializer.data['id']}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        instance = get_object_or_404(MasterTable, pk=pk)
        serializer = MasterTableSerializer(instance, data=request.data)
        if serializer.is_valid():
            updated_audit_fields(instance, serializer)
            serializer.save()
            create_delete_dynamic_table(serializer.data)
            logger.info(f"Put Updated MasterTable with ID {serializer.data['id']}")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        instance = get_object_or_404(MasterTable, pk=pk)
        serializer = MasterTableSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            updated_audit_fields(instance, serializer)
            serializer.save()
            create_delete_dynamic_table(serializer.data)
            logger.info(f"Patch Updated MasterTable with ID {serializer.data['id']}")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        instance = get_object_or_404(MasterTable, pk=pk)
        if not instance:
            logger.error(f"Instance is already deleted in MasterTable with ID {pk}")
            return Response("Instance is already deleted", status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = MasterTableSerializer(instance, data=request.data,partial=True)
            if serializer.is_valid():
                print(serializer.data)
                delete_dynamic_table(serializer.data)
            instance.delete()
            logger.info(f"Deleted MasterTable with ID {pk}")
            return Response("Deleted successfully", status=status.HTTP_204_NO_CONTENT)

class DynamicTableListCreateView(APIView):
    def get(self, request, table_name):
        try:
            model = create_dynamic_model(table_name)
            instances = model.objects.all()
            serializer = DynamicTableSerializer(instances, many=True)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error retrieving data from {table_name}: {e}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, table_name):
        try:
            model = create_dynamic_model(table_name)
            serializer = DynamicTableSerializer(data=request.data)
            if serializer.is_valid():
                instance = model(**serializer.validated_data)
                instance.save()
                logger.info(f"Created instance in {table_name} with ID {instance.id}")
                return Response(DynamicTableSerializer(instance).data, status=status.HTTP_201_CREATED)
            logger.error(f"Serializer errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating data in {table_name}: {e}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DynamicTableDetailView(APIView):
    def get(self, request, table_name, pk):
        try:
            model = create_dynamic_model(table_name)
            instance = model.objects.get(pk=pk)
            serializer = DynamicTableSerializer(instance)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, table_name, pk):
        try:
            model = create_dynamic_model(table_name)
            instance = model.objects.get(pk=pk)
            serializer = DynamicTableSerializer(instance, data=request.data)
            if serializer.is_valid():
                for key, value in serializer.validated_data.items():
                    setattr(instance, key, value)
                instance.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, table_name, pk):
        try:
            model = create_dynamic_model(table_name)
            instance = model.objects.get(pk=pk)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class SyncMasterTableView(APIView):
    def post(self, request):
        url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
        try:
            # Fetch the JSON data with streaming enabled
            response = requests.get(url, stream=True, timeout=10)
            response.raise_for_status()  # Check for successful request

            # Incrementally parse the JSON data
            items = ijson.items(response.raw, 'item')

            for item in items:
                newitem = {
                    "token_id": item["token"],
                    "constant_name": item["symbol"],
                    "stock_name": item["name"],
                    "exchange": item["exch_seg"]                    
                }
                if newitem["exchange"] == "NSE":
                    del newitem["exchange"]
                    print(newitem)
                logger.info(newitem)

                serializer = MasterTableSerializer(data=newitem)
                if serializer.is_valid():
                   serializer.save()
                else:
                   print(serializer.errors)

            return Response("Data synced successfully", status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)