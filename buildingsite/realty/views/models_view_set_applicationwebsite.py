"""
Вьюшка Заявки с сайта
"""
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from realty.models import ApplicationWebsite
from realty.paginations.applicationwebsite import ApplicationPagination
from realty.serializers.applicationwebsite import ApplicationWebsiteSerializer, \
    StatusApplicationSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


class ApplicationModelViewSet(viewsets.ModelViewSet):
    """
    Вьюшка для ApplicationWebsite
    """
    queryset = ApplicationWebsite.objects.all()
    serializer_class = ApplicationWebsiteSerializer
    pagination_class = ApplicationPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name_client', 'number_phone']

    @action(methods=['get'], detail=False)
    def application_website_filter(self, request):

        """Фильтр отражает заявки, которые одновременно имеют статус
        "Принято" и соответствуют хотя бы одному из условий
        (либо имя "Адександр", либо номер телефона не содержит "9911")"""

        filter_condition = (
            Q(status_application='accepted') &
            (Q(name_client='Александер') | ~Q(number_phone__contains='9911'))
        )

        name_client = request.query_params.get('name_client', None)
        number_phone = request.query_params.get('number_phone', None)

        if name_client:
            # Фильтрация по имени клиента
            filter_condition &= Q(name_client__icontains=name_client)
        if number_phone:
            # Фильтрация по номеру телефона
            filter_condition &= ~Q(number_phone__contains=number_phone)

        application_filter = ApplicationWebsite.objects.filter(filter_condition)
        serializer = ApplicationWebsiteSerializer(application_filter, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def update_status(self, request, pk=None):
        """Запрос post изменяем статус заявки"""
        application = self.get_object()
        serializer = StatusApplicationSerializer(application, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
                # Возвращаем ответ только с обновленным полем status_application
            return Response(
                {"message": "Статус изменён"},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
