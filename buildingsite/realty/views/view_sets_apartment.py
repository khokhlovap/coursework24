from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from django.db.models import Q
from django_filters import rest_framework as filters
from realty.models import Apartment
from realty.serializers.apartment import ApartmentSerializer
from realty.views.filter_price import PriceFilter


class ApartmentViewSet(viewsets.ModelViewSet):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()
    filterset_class = PriceFilter
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['price', 'square']
    
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
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
