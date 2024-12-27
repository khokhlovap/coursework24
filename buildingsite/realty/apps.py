"""
Конфигурация приложения Django
"""
from django.apps import AppConfig


class RealtyConfig(AppConfig):
    """
    Конфигурация приложения realty
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'realty'
