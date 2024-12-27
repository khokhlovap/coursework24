"""
Фильтр для таблицы Infobuilding
"""
from realty.models import InfoBuilding
from realty.serializers.infobuilding import InfobuildingSerializer
from rest_framework import generics


class InfobuildingByNumberView(generics.ListAPIView):
    """Фильтр по параметру в url"""
    serializer_class=InfobuildingSerializer

    def get_queryset(self):
        code_building = self.kwargs.get('code_building')
        return InfoBuilding.objects.filter(code_building=code_building)
