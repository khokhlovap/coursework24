from rest_framework import viewsets, status
from rest_framework.response import Response
from realty.models import ApplicationWebsite
from realty.serializers.applicationwebsite import ApplicationWebsiteSerializer
from rest_framework.decorators import action
from realty.paginations.applicationwebsite import ApplicationPagination

class ApplicationModelViewSet(viewsets.ModelViewSet):
    queryset = ApplicationWebsite.objects.all()
    serializer_class = ApplicationWebsiteSerializer
    pagination_class = ApplicationPagination

    @action(methods=['post'], detail=True)
    def update_status(self, request, pk=None):
        application = self.get_object() 
        new_status = request.data.get('status') 
        if new_status:
            application.status = new_status
            application.save() 

            return Response({'new_status': application.status}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)