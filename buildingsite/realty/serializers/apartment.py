from rest_framework import serializers
from realty.models import Apartment

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ['number_rooms', 'number_floor', 'square', 'price', 'apartment_code']