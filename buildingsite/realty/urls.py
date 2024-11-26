from django.urls import path, include
from rest_framework.routers import DefaultRouter
from realty.views.view_sets_apartment import ApartmentViewSet
from realty.views.view_sets_infobuilding import InfobuildingViewSet


router = DefaultRouter()
router.register(r'apartment-viewset', ApartmentViewSet, basename='apartment-viewset')
urlpatterns = [
    path('', include(router.urls)),
]

router.register(r'infobuilding-viewset', InfobuildingViewSet, basename='infobuilding-viewset')
urlpatterns = [
    path('', include(router.urls)),
]