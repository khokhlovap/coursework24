"""
Пагинация
"""
from rest_framework import pagination


class ApplicationPagination(pagination.PageNumberPagination):
    """Пагинация на странице заявок с сайта"""
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 50
