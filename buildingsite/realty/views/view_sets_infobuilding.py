from rest_framework import viewsets
from realty.models import InfoBuilding
from realty.serializers.infobuilding import InfobuildingSerializer

class InfobuildingModelViewSet(viewsets.ModelViewSet):
    queryset = InfoBuilding.objects.all()
    serializer_class = InfobuildingSerializer