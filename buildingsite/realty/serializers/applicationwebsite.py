"""
Сериализатор Заявки с сайта и Статтус заявок
"""
from realty.models import ApplicationWebsite
from rest_framework import serializers


class ApplicationWebsiteSerializer(serializers.ModelSerializer):
    """
    Модель ApplicationWebsite
    """
    class Meta:
        """
        Поля таблицы для отражения
        """
        model = ApplicationWebsite
        fields = ['id', 'name_client', 'number_phone', 'status_application', 'date_create3']


class StatusApplicationSerializer(serializers.ModelSerializer):
    """
    Модель StatusApplication
    """
    class Meta:
        """
        Поля таблицы для отражения
        """
        model = ApplicationWebsite
        fields = ['status_application']
