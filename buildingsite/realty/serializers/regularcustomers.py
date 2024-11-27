from rest_framework import serializers
from realty.models import RegularCustomers

class RegularCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegularCustomers
        fields = ['name_client', 'surname_client', 'number_phone', 'email_client']