from rest_framework import generics
from realty.serializers.infobuilding import InfobuildingSerializer
from realty.models import InfoBuilding

class InfobuildingByNumberView(generics.ListAPIView):
    serializer_class=InfobuildingSerializer

    def get_queryset(self):
        number = self.kwargs['number']
        return InfoBuilding.objects.filter(code_building=number)
