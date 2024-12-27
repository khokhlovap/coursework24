"""
Вьюшка Информация о здании
"""
from realty.models import InfoBuilding
from realty.serializers.infobuilding import InfobuildingSerializer
from rest_framework import viewsets


class InfobuildingModelViewSet(viewsets.ModelViewSet):
    """
    Вьюшка InfoBuilding
    """
    queryset = InfoBuilding.objects.all()
    serializer_class = InfobuildingSerializer
