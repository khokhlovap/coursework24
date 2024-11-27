from django.urls import path, include
from rest_framework.routers import DefaultRouter
from realty.views.view_sets_apartment import ApartmentViewSet
from realty.views.view_sets_infobuilding import InfobuildingViewSet
from realty.views.filter_by_number_room import InfobuildingByNumberView
from realty.views.model_view_set_customers import RegularCustomersModelViewSet

router = DefaultRouter()
router.register(r'apartment-viewset', ApartmentViewSet, basename='apartment-viewset')
urlpatterns = [
    path('', include(router.urls)),
]

router.register(r'infobuilding-viewset', InfobuildingViewSet, basename='infobuilding-viewset')
urlpatterns = [
    path('', include(router.urls)),
    path('number/<int:number>/', InfobuildingByNumberView.as_view(), name='infobuilding-by-number')
]

router.register(r'regularcustomers-viewset', RegularCustomersModelViewSet, basename='regularcustomers-viewset')
urlpatterns = [
    path('', include(router.urls)),
]