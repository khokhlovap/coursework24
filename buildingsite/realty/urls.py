"""
Подключение urls
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from realty.views.filter_by_code_building import InfobuildingByNumberView
from realty.views.models_view_set_applicationwebsite import ApplicationModelViewSet
from realty.views.view_sets_apartment import ApartmentViewSet
from realty.views.model_view_set_customers import RegularCustomersModelViewSet
from realty.views.view_sets_infobuilding import InfobuildingModelViewSet
InfobuildingModelViewSet
from realty.views.views import apartment_list, apartment_detail


router = DefaultRouter()
router.register(r'apartment-viewset', ApartmentViewSet, basename='apartment-viewset')
router.register(r'infobuilding-viewset', InfobuildingModelViewSet, basename='infobuilding-viewset')
router.register(r'regularcustomers-viewset', RegularCustomersModelViewSet,
                basename='regularcustomers-viewset')
router.register(r'applicationwebsite-viewset', ApplicationModelViewSet,
                basename='applicationwebsite-viewset')

urlpatterns = [
    path('', include(router.urls)),
    path('apartment/', apartment_list, name='apartment_list'),  # Главная страница со списком апартаментов
    path('apartment/<int:apartment_id>/', apartment_detail, name='apartment_detail'),
    path('code_building/<int:code_building>/', InfobuildingByNumberView.as_view(),
         name='infobuilding-by-number'),
]
