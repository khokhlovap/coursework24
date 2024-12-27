"""
Вьюшка Апартаменты
"""
from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from realty.models import Apartment
from realty.serializers.apartment import ApartmentSerializer
from realty.views.filter_price import PriceFilter
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response


class ApartmentViewSet(viewsets.ModelViewSet):
    """
    Вьюшка Apartment
    """
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()
    filterset_class = PriceFilter
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['price', 'square']
    # def list(self, request):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = ApartmentSerializer(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    @action(methods=['get'], detail=False)
    def for_process(self, request):
        """
        Фильтр с Q запросом
        """
        filter_condition = (
                (Q(square__lte=50) | Q(number_rooms__lte=2)) &
                Q(code_building__city='Москва') & ~Q(statusapartment__status_apartment='Продано')
        )
        apartments_filter = Apartment.objects.filter(filter_condition)
        serializer = ApartmentSerializer(apartments_filter, many=True)
        return Response(serializer.data)

    def get_apartment(self, apartment_id):
        """
        Получает апартамент. Сначала проверяет кэш, затем базу данных. не работает
        """
        # Формируем ключ для кэша
        cache_key = f"apartment_{apartment_id}"
        # Проверяем наличие данных в кэше
        apartment = cache.get(cache_key)
        if apartment is None:
            print("Cache miss - getting from database")

            # Если данных нет в кэше, извлекаем из базы
            apartment = get_object_or_404(Apartment, pk=apartment_id)
            # Сохраняем в кэш на 15 минут
            cache.set(cache_key, apartment, timeout=60 * 15)
        else:
            print("Cache hit - getting from Redis")
        return apartment


    # @action(methods=['get'], detail=True)
    # def retrieve(self, request, pk=None):
    #     """Получение рецепта по ID с кэшированием"""
    #     apartment = self.get_apartment(pk)
    #     serializer = self.get_serializer(recipe)
    #
    #     return Response(serializer.data)
