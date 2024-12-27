"""
Сериализатор для модели Apartment
"""
from realty.models import Apartment
from rest_framework import serializers


class ApartmentSerializer(serializers.ModelSerializer):
    """
    Модель Apartment
    """
    class Meta:
        """
        Поля таблицы, которые будут отражаться
        """
        model = Apartment
        fields = ['number_rooms', 'number_floor', 'square', 'price', 'apartment_code']
