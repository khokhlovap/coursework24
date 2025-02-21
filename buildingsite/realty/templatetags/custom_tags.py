"""Теги"""

from django import template
from realty.models import ApplicationWebsite, Apartment, RegularCustomers, StatusApartment

register = template.Library()

@register.simple_tag
def count_applications():
    """Возвращает количество заявок с сайта (бд)."""
    return ApplicationWebsite.objects.count()

@register.simple_tag(takes_context=True)
def greet_with_context(context, name):
    """Возвращает приветственное сообщение с использованием контекста."""
    user = context.get('user', 'Гость')
    return f"Привет, {name}! Вы вошли как {user}."

@register.simple_tag
def get_customer():
    """Возвращает все квартиры."""
    return RegularCustomers.objects.all()

@register.simple_tag
def count_sold_apartment():
    """Возвращает количество проданных апартаментов"""
    return StatusApartment.objects.filter(status_apartment='sold').count()

@register.filter
def add_class(field, css_class):
    """Добавляет указанный CSS-класс к полю формы."""
    return field.as_widget(attrs={'class': css_class})

@register.filter
def format_price(value):
    """Преобразуем формат цены на сайте"""
    if value is None:
        return ''
    return f"{value:,.0f}".replace(',', ' ').replace('.', ',') + ' ₽'