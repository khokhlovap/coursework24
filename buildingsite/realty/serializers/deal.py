from rest_framework import serializers
from realty.models import Deal2

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal2
        fields = ['id', 'apartment', 'client', 'data_deal']  
        depth = 1  # включаем связанные объекты