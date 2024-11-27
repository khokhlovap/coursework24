from rest_framework import viewsets
from realty.models import RegularCustomers
from realty.serializers.regularcustomers import RegularCustomersSerializer
from rest_framework import filters

class RegularCustomersModelViewSet(viewsets.ModelViewSet):
    queryset = RegularCustomers.objects.all()
    serializer_class = RegularCustomersSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_client']