from django import template
from realty.models import ApplicationWebsite, Apartment, RegularCustomers

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
