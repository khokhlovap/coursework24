"""
Вьюшка Постоянные клиенты
"""
from rest_framework import viewsets
from rest_framework import filters
from realty.models import RegularCustomers
from realty.serializers.regularcustomers import RegularCustomersSerializer


class RegularCustomersModelViewSet(viewsets.ModelViewSet):
    """
    Вьюшка для Постоянных клиентов
    """
    queryset = RegularCustomers.objects.all()
    serializer_class = RegularCustomersSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_client']
