from django.shortcuts import get_list_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from realty.models import Apartment
from realty.serializers.apartment import ApartmentSerializer

class ApartmentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Apartment.objects.all()
        serializer = ApartmentSerializer(queryset, many=True)
        return Response(serializer.data)