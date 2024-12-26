import django_filters
from realty.models import Apartment


class PriceFilter(django_filters.FilterSet):
    """Фильтр - диапазон цен, фильтрация стоимости апартаментов"""
    price_range = django_filters.RangeFilter(field_name='price', label='Диапазон цены')
    class Meta:
        model = Apartment
        fields = ['price_range']
