from django.shortcuts import get_list_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from realty.models import InfoBuilding
from realty.serializers.infobuilding import InfobuildingSerializer

class InfobuildingViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InfoBuilding.objects.all()
        serializer = InfobuildingSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = InfobuildingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = InfoBuilding.objects.all()
        infobuilding = get_list_or_404(queryset, pk=pk)
        serializer = InfobuildingSerializer(infobuilding, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        infobuilding = get_list_or_404(InfoBuilding, pk=pk)
        serializer = InfobuildingSerializer(infobuilding, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        infobuilding = get_list_or_404(InfoBuilding, pk=pk)
        infobuilding.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)