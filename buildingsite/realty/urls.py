from django.urls import path, include
from rest_framework.routers import DefaultRouter
from realty.views.view_sets_apartment import ApartmentViewSet
from realty.views.view_sets_infobuilding import InfobuildingModelViewSet
from realty.views.filter_by_code_building import InfobuildingByNumberView
from realty.views.model_view_set_customers import RegularCustomersModelViewSet
from realty.views.models_view_set_applicationwebsite import ApplicationModelViewSet

router = DefaultRouter()
router.register(r'apartment-viewset', ApartmentViewSet, basename='apartment-viewset')
router.register(r'infobuilding-viewset', InfobuildingModelViewSet, basename='infobuilding-viewset')
router.register(r'regularcustomers-viewset', RegularCustomersModelViewSet, basename='regularcustomers-viewset')
router.register(r'applicationwebsite-viewset', ApplicationModelViewSet, basename='applicationwebsite-viewset')

urlpatterns = [
    path('', include(router.urls)),
    path('code_building/<int:code_building>/', InfobuildingByNumberView.as_view(), name='infobuilding-by-number')
]