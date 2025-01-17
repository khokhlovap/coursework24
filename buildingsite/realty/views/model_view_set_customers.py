"""
Вьюшка Постоянные клиенты
"""
from rest_framework import viewsets, status
from rest_framework import filters
from django.shortcuts import redirect
from rest_framework.response import Response
from realty.models import RegularCustomers
from realty.serializers.regularcustomers import RegularCustomersSerializer
from django.urls import reverse
from django.views import View
from django.http import HttpResponse


class RegularCustomersModelViewSet(viewsets.ModelViewSet):
    """
    Вьюшка для Постоянных клиентов
    """
    queryset = RegularCustomers.objects.all()
    serializer_class = RegularCustomersSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_client']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

#         # Проверяем имя клиента
#         # Проверяем имя клиента
#         if serializer.validated_data['name_client'].upper() == "МАРИЯ":
#             return Response({'redirect_url': reverse('maria_data_page')}, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
#
# class MariaDataView(View):
#     def get(self, request):
#         return HttpResponse("<h1>Данные о Марии</h1>")
