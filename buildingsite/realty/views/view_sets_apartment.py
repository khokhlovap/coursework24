from django.shortcuts import get_list_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from realty.models import Apartment
from django.db.models import Q
from realty.serializers.apartment import ApartmentSerializer

class ApartmentViewSet(viewsets.ViewSet):
    serializer_class = ApartmentSerializer
    def list(self, request):
        queryset = Apartment.objects.all()

        filter_condition = (
            (Q(square__lte=50) | Q(number_rooms__lte=2)) & 
            Q(code_building__city='Москва') & ~Q(statusapartment__status_apartment='Продано')
        )
        apartments = queryset.filter(filter_condition)

        serializer = ApartmentSerializer(apartments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)