from import_export.resources import ModelResource
from realty.models import Apartment


class ApartmentResource(ModelResource):
    class Meta:
        model = Apartment
        fields = ('number_rooms', 'number_floor', 'square', 'price', 'code_building', 'apartment_code')

    def dehydrate_square(self, apartment):
        # Форматируем площадь с указанием единиц измерения - кв.м
        return f'{apartment.square:.2f} кв.м'
    
    def dehydrate_price(self, apartment):
        # Форматируем цену с указанием валюты - рубли
        return f'{apartment.price:.2f} руб.'
        