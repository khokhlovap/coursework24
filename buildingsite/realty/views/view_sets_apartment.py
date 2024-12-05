from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from realty.models import Apartment, RegularCustomers, Deal2
from django.db.models import Q
from realty.serializers.apartment import ApartmentSerializer
from django_filters import rest_framework as filters

from rest_framework.decorators import action

class ApartmentFilter(filters.FilterSet):
    number_rooms = filters.NumberFilter()

    class Meta:
        model = Apartment
        fields = ['number_rooms']  

class ApartmentViewSet(viewsets.ViewSet):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ApartmentFilter

    def list(self, request):
        queryset = Apartment.objects.all()
        serializer = ApartmentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['get'], detail=False)
    def for_process(self, request):
            
        filter_condition = (
            (Q(square__lte=50) | Q(number_rooms__lte=2)) & 
            Q(code_building__city='Москва') & ~Q(statusapartment__status_apartment='Продано')
        )
        
        apartments_filter = Apartment.objects.filter(filter_condition)
        serializer = ApartmentSerializer(apartments_filter, many=True)
        return Response(serializer.data)