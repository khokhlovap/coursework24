"""
Сериализатор Информация о зданиии
"""
import re
from realty.models import InfoBuilding
from rest_framework import serializers


class InfobuildingSerializer(serializers.ModelSerializer):
    """
    Модель Infobuilding
    """
    class Meta:
        """
         Поля таблицы для отражения
        """
        model = InfoBuilding
        fields = ['code_building', 'city', 'street', 'number_building']

    def validate_code_building(self, value):
        """
        Валидация
        """
        if InfoBuilding.objects.filter(code_building=value).exists():
            raise serializers.ValidationError("Код здания уже существует. "
                                              "Пожалуйста, используйте уникальный код.")
        return value
    def validate_street(self, value):
        """
        Валидация
        """
        if re.search(r'\d', value):
            raise serializers.ValidationError("Название улицы не должно содержать цифры.")
        return value

    def validate_number_building(self, value):
        """
        Валидация
        """
        try:
            number = int(value)  # Пробуем преобразовать строку в целое число
        except ValueError:
            raise serializers.ValidationError("Номер дома должен быть числом.")
        if number <= 0:
            raise serializers.ValidationError("Номер дома должен быть больше нуля.")
        return value  # Возвращаем оригинальное значение
