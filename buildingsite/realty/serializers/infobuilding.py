from rest_framework import serializers
from realty.models import InfoBuilding
import re

class InfobuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoBuilding
        fields = ['code_building', 'city', 'street', 'number_building']

    def validate_code_building(self, value):
        if InfoBuilding.objects.filter(code_building=value).exists():                
            raise serializers.ValidationError("Код здания уже существует. Пожалуйста, используйте уникальный код.")
        return value
    
    def validate_street(self, value):
        if re.search(r'\d', value):
            raise serializers.ValidationError("Название улицы не должно содержать цифры.")
        return value
    
    def validate_number_building(self, value):
        if value <= 0:
            raise serializers.ValidationError("Номер дома должен быть больше нуля.")
        return value