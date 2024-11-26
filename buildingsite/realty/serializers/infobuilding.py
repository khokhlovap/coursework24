from rest_framework import serializers
from realty.models import InfoBuilding

class InfobuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoBuilding
        fields = ['code_building', 'city', 'street', 'number_building']