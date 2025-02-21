"""
Подключение urls
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from realty.views.filter_by_code_building import InfobuildingByNumberView
from realty.views.models_view_set_applicationwebsite import ApplicationModelViewSet
from realty.views.view_sets_apartment import ApartmentViewSet
from realty.views.model_view_set_customers import RegularCustomersModelViewSet
from realty.views.view_sets_infobuilding import InfobuildingModelViewSet
InfobuildingModelViewSet
from realty.views.views import apartment_list, apartment_detail
from realty.views.homepage_views import apartment
from realty.views.apartment_id import apartment_id
from realty.views.apartmentcorect import apartment_correct, delete_apartment
from realty.forms.forma_newapartment import add_apartment



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
    path('homepage/', apartment, name='apartment'),
    path('code_building/<int:code_building>/', InfobuildingByNumberView.as_view(),
         name='infobuilding-by-number'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('homepage/<int:apartment_id>/', apartment_id, name='apartment_id'),
    path('homepage/<int:apartment_id>/', apartment_id, name='apartment'),
    path('apartmentcorrect/', apartment_correct, name='apartment_correct'),
    path('apartmentcorrect/delete/<int:pk>/', delete_apartment, name='delete_apartment'),
    path('apartmentcorrect/add/', add_apartment, name='add_apartment'),
]

#Для загрузки фото в форму (создание нового апартамента)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
