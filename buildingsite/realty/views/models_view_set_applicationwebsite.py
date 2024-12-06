from rest_framework import viewsets, status
from rest_framework.response import Response
from realty.models import ApplicationWebsite
from realty.serializers.applicationwebsite import ApplicationWebsiteSerializer
from rest_framework.decorators import action
from realty.paginations.applicationwebsite import ApplicationPagination
from django.db.models import Q

class ApplicationModelViewSet(viewsets.ModelViewSet):
    queryset = ApplicationWebsite.objects.all()
    serializer_class = ApplicationWebsiteSerializer
    pagination_class = ApplicationPagination

    @action(methods=['get'], detail=False)
    def application_website_filter(self, request):
    
        """
        Фильтр отражает заявки, которые одновременно имеют статус "Принято" и соответствуют хотя бы одному из условий 
        (либо имя "Мария", либо номер телефона не содержит "2345")
        """

        filter_condition = (
            Q(status_application='accepted') & 
            (Q(name_client='Мария') | ~Q(number_phone__contains='3471'))
        )
        
        application_filter = ApplicationWebsite.objects.filter(filter_condition)
        serializer = ApplicationWebsiteSerializer(application_filter, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def update_status(self, request, pk=None):
        application = self.get_object() 
        serializer = ApplicationWebsiteSerializer(application, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response({"message": "статус изменен"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_serializer_class(self):

        if self.action == 'status_application':
            return ApplicationWebsiteSerializer
        return super().get_serializer_class()