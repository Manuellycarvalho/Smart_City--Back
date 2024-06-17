import django_filters
from App_Smart.models import Sensor, TemperaturaData, ContadorData, UmidadeData, LuminosidadeData
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from App_Smart.api.serializers import (
    SensorSerializer, 
    TemperaturaDataSerializer, 
    ContadorDataSerializer, 
    UmidadeDataSerializer,
    LuminosidadeDataSerializer
)
from django.db.models import Q
from django_filters import rest_framework as filters

class Sensorfilter(django_filters.FilterSet):
    responsavel = django_filters.CharFilter(field_name='responsavel', lookup_expr='icontains')
    status_operacional = django_filters.CharFilter(field_name='status_operacional', lookup_expr='exact')
    tipo = django_filters.CharFilter(field_name='tipo', lookup_expr='exact')
    localizacao = django_filters.CharFilter(field_name='localizacao', lookup_expr='icontains')

    class Meta:
        model = Sensor
        fields = ['responsavel', 'status_operacional', 'tipo', 'localizacao']

class TemperaturaDataFilter(django_filters.FilterSet):
    timestamp_gte = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='gte')
    timestamp_lt = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='lt')
    sensor = django_filters.NumberFilter(field_name="sensor")
    valor_gte = django_filters.NumberFilter(field_name='valor', lookup_expr='gte')
    valor_lt = django_filters.NumberFilter(field_name='valor', lookup_expr='lt')

    class Meta:
        model = TemperaturaData
        fields = ['timestamp', 'sensor', 'valor_gte', 'valor_lt']

class TemperaturaFilterView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        sensor_id = request.data.get('sensor_id', None)
        valor_gte = request.data.get('valor_gte', None)
        valor_lt = request.data.get('valor_lt', None)
        timestamp_gte = request.data.get('timestamp_gte', None)
        timestamp_lt = request.data.get('timestamp_lt', None)

        filters = Q()
        if sensor_id:
            filters &= Q(sensor_id=sensor_id)
        if valor_gte:
            filters &= Q(valor__gte=valor_gte)
        if valor_lt:
            filters &= Q(valor__lt=valor_lt)
        if timestamp_gte:
            filters &= Q(timestamp__gte=timestamp_gte)
        if timestamp_lt:
            filters &= Q(timestamp__lt=timestamp_lt)

        queryset = TemperaturaData.objects.filter(filters)
        serializer = TemperaturaDataSerializer(queryset, many=True)
        return Response(serializer.data)

class ContadorFilterView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        sensor_id = request.data.get('sensor_id', None)
        timestamp_gte = request.data.get('timestamp_gte', None)
        timestamp_lt = request.data.get('timestamp_lt', None)

        filters = Q()
        if sensor_id:
            filters &= Q(sensor_id=sensor_id)
        if timestamp_gte:
            filters &= Q(timestamp__gte=timestamp_gte)
        if timestamp_lt:
            filters &= Q(timestamp__lt=timestamp_lt)

        queryset = ContadorData.objects.filter(filters)
        count = queryset.count()
        serializer = ContadorDataSerializer(queryset, many=True)

        response_data = {
            'count': count,
            'results': serializer.data
        }

        return Response(response_data)

class UmidadeFilterView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        sensor_id = request.data.get('sensor_id', None)
        valor_gte = request.data.get('valor_gte', None)
        valor_lt = request.data.get('valor_lt', None)
        timestamp_gte = request.data.get('timestamp_gte', None)
        timestamp_lt = request.data.get('timestamp_lt', None)

        filters = Q()
        if sensor_id:
            filters &= Q(sensor_id=sensor_id)
        if valor_gte:
            filters &= Q(valor__gte=valor_gte)
        if valor_lt:
            filters &= Q(valor__lt=valor_lt)
        if timestamp_gte:
            filters &= Q(timestamp__gte=timestamp_gte)
        if timestamp_lt:
            filters &= Q(timestamp__lt=timestamp_lt)

        queryset = UmidadeData.objects.filter(filters)
        serializer = UmidadeDataSerializer(queryset, many=True)
        return Response(serializer.data)

class LuminosidadeFilterView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        sensor_id = request.data.get('sensor_id', None)
        valor_gte = request.data.get('valor_gte', None)
        valor_lt = request.data.get('valor_lt', None)
        timestamp_gte = request.data.get('timestamp_gte', None)
        timestamp_lt = request.data.get('timestamp_lt', None)

        filters = Q()
        if sensor_id:
            filters &= Q(sensor_id=sensor_id)
        if valor_gte:
            filters &= Q(valor__gte=valor_gte)
        if valor_lt:
            filters &= Q(valor__lt=valor_lt)
        if timestamp_gte:
            filters &= Q(timestamp__gte=timestamp_gte)
        if timestamp_lt:
            filters &= Q(timestamp__lt=timestamp_lt)

        queryset = LuminosidadeData.objects.filter(filters)
        serializer = LuminosidadeDataSerializer(queryset, many=True)
        return Response(serializer.data)
