from rest_framework import serializers
from realty.models import ApplicationWebsite

class ApplicationWebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationWebsite
        fields = ['id', 'name_client', 'number_phone', 'status_application', 'date_create3']

class StatusApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationWebsite
        fields = ['status_application']
