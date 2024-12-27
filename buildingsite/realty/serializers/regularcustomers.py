"""
Сериализатор постоянные клиенты
"""
from realty.models import RegularCustomers
from rest_framework import serializers


class RegularCustomersSerializer(serializers.ModelSerializer):
    """
    Поля таблицы, которые будут отражаться
    """
    class Meta:
        """"
        Поля таблицы для отражения
        """
        model = RegularCustomers
        fields = ['name_client', 'surname_client', 'number_phone', 'email_client']
