"""
admin.py

Этот модуль содержит настройки админки для моделей бд.
Содержит классы для управления отображением и функциональностью админ-интерфейса.
"""

from datetime import datetime
from django.contrib import admin
from import_export import resources
from django.urls import reverse
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from simple_history.admin import SimpleHistoryAdmin
from realty.views.pdf import export_to_pdf
from .models import InfoBuilding, Apartment, StatusApartment, RegularCustomers, Deal2, \
    ApplicationWebsite, ApartmentPhoto, BuildingPhoto


class ApartmentInline(admin.TabularInline):
    """
    Создаем inline, связь многие ко многим таблица Apartment и Infobuilding
    """

    model = Apartment
    extra = 1  # Количество пустых форм для добавления новых объектов

class BuildingtPhotoInline(admin.TabularInline):
    """
    Создаем inline, связь многие ко многим
    """
    model = BuildingPhoto
    extra = 1  # Количество пустых форм для добавления новых объектов

class InfoBuildingAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    """
    Админка таблицы Информация о здании
    """
    list_display = ('formatted_code', 'city', 'street', 'number_building', 'formatted_date_change', 'file_document', 'website_url')
    list_filter = ('city', 'code_building',)
    list_display_links = ('city',)
    inlines = [ApartmentInline]  # Добавляем inline
    actions = [export_to_pdf]
    inlines = [BuildingtPhotoInline]  # Добавляем inline

    @admin.display(description='Код здания')  # Указываем описание для заголовка столбца
    def formatted_code(self, obj):
        """
        Форматируем вывод
        """
        return f'Код: {obj.code_building}'

    @admin.display(description='Дата последнего обновления')
    def formatted_date_change(self, obj):
        """
        Форматируем формат даты
        """
        return obj.updated.strftime('%d.%m.%Y')

class ApartmentPhotoInline(admin.TabularInline):
    """
    Создаем inline, связь многие ко многим таблица Apartment и Infobuilding
    """
    model = ApartmentPhoto
    extra = 1  # Количество пустых форм для добавления новых объектов


class ApartmentResource(resources.ModelResource):
    """
    Подготовка бд к экспорту
    """
    class Meta: # pylint: disable=too-few-public-methods
        """
        Поля для экспорта
        """
        model = Apartment
        fields = ('number_rooms', 'number_floor', 'square',
                  'price', 'code_building', 'apartment_code')

    def dehydrate_square(self, obj):
        """Форматируем площадь с указанием единиц измерения - кв.м """
        return f'{obj.square} кв.м'

    def dehydrate_price(self, apartment):
        """Форматируем цену с указанием валюты - рубли"""
        return f'{apartment.price:.2f} руб.'


class ApartmentAdmin(SimpleHistoryAdmin, ImportExportModelAdmin,
                     ExportActionMixin, admin.ModelAdmin):
    """
    Админка таблица Апартаменты
    """

    resource_class = ApartmentResource
    list_display = ('id', 'number_rooms', 'number_floor', 'square', 'price',
                    'code_building', 'building_info', 'apartment_code')
    list_filter = ('number_rooms', 'number_floor', 'code_building',)
    # readonly_fields = ('square',)
    search_fields = ('apartment_code',)
    raw_id_fields = ('code_building',)
    inlines = [ApartmentPhotoInline]  # Добавляем inline

    def get_export_filename(self):
        # Получаем текущую дату для добавления в имя файла
        current_date = datetime.now().strftime('%d.%m.%Y')
        return f'Apartments_export_{current_date}.csv'

    def get_export_queryset(self, request):
        """Экспортируем только записи, где количество комнат >= 2"""
        queryset = super().get_export_queryset(request)
        print(request)
        return queryset.filter(number_rooms__gte=2)


class ApartmentPhotoAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    """Класс медиа"""
    list_display = ('apartment', 'image', 'description')

class BuildingPhotoAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    """Класс медиа"""
    list_display = ('building', 'image', 'description')

class StatusApartmentAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    """
    Админка таблица Статус апартаментов
    """
    list_display = ('id_apartment', 'status_apartment', 'formatted_date_change', 'id_client')
    date_hierarchy = 'data_change'
    raw_id_fields = ('id_client', 'id_apartment',)
    list_filter = ('status_apartment',)

    @admin.display(description='Дата изменения')
    def formatted_date_change(self, obj):
        """
        Форматируем ормат даты
        """
        return obj.data_change.strftime('%d.%m.%Y')


class RegularCustomersResource(resources.ModelResource):
    """
    Подготовка таблицы Постоянные клиенты для экспорта
    """
    class Meta: # pylint: disable=too-few-public-methods
        """
        Поля таблицы для экспорта
        """
        model = RegularCustomers
        fields = ('name_client', 'surname_client', 'number_phone', 'email_client')


class RegularCustomersInline(admin.TabularInline):
    """
       Создаем inline таблица Постоянные клиенты
    """
    model = Deal2
    extra = 1  # Количество пустых форм для добавления новых объектов


class RegularCustomersAdmin(SimpleHistoryAdmin, ImportExportModelAdmin,
                            ExportActionMixin, admin.ModelAdmin):
    """
    Админка Постоянные клиенты
    """
    resource_class = RegularCustomersResource
    list_display = ('id', 'name_client', 'surname_client', 'number_phone', 'email_client')
    search_fields = ('name_client', 'surname_client', 'id')
    inlines = [RegularCustomersInline]

    def get_export_filename(self):
        # Получаем текущую дату для добавления в имя файла
        current_date = datetime.now().strftime('%d.%m.%Y')
        return f'RegularCustomers_export_{current_date}.csv'


class Deal2Admin(SimpleHistoryAdmin, admin.ModelAdmin):
    """
    Админка Сделка
    """
    list_display = ('apartment', 'client', 'formatted_date_change')
    raw_id_fields = ('client', 'apartment',)
    date_hierarchy = 'data_deal'

    @admin.display(description='Дата изменения')
    def formatted_date_change(self, obj):
        """
        Форматируем формат даты
        """
        return obj.data_deal.strftime('%d.%m.%Y')


class ApplicationWebsiteResource(resources.ModelResource):
    """
    Подготовка таблицы Заявки с сайта для экспорта в эксель
    """
    class Meta: # pylint: disable=too-few-public-methods
        """
        Поля таблицы для экспорта
        """
        model = ApplicationWebsite
        fields = ('name_client', 'number_phone', 'status_application', 'date_create3')

    def dehydrate_status_application(self, application_website):
        """Изменяем статус при экспорте"""
        if application_website.status_application == 'accepted':
            return "Принято"

        return "Отклонено"

    def dehydrate_date_create3(self, application_website):
        """Изменяем формат даты на дд.мм.гг"""
        return application_website.date_create3.strftime('%d.%m.%y')


class ApplicationWebsiteAdmin(SimpleHistoryAdmin, ImportExportModelAdmin,
                              ExportActionMixin, admin.ModelAdmin):
    """
    Админка заявки с сайта
    """
    resource_class = ApplicationWebsiteResource
    list_display = ('formatted_date_change', 'name_client', 'number_phone', 'status_application')
    date_hierarchy = 'date_create3'
    readonly_fields = ('date_create3',)
    list_filter = ('status_application',)

    @admin.display(description='Дата создания заявки')
    def formatted_date_change(self, obj):
        """
        Форматируем формат даты
        """
        return obj.date_create3.strftime('%d.%m.%Y')

    def get_export_filename(self,  *args, **kwargs):
        # Получаем текущую дату для добавления в имя файла
        current_date = datetime.now().strftime('%d.%m.%Y')
        return f'ApplicationWebsite_export_{current_date}.csv'


admin.site.register(InfoBuilding, InfoBuildingAdmin)
admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(StatusApartment, StatusApartmentAdmin)
admin.site.register(RegularCustomers, RegularCustomersAdmin)
admin.site.register(Deal2, Deal2Admin)
admin.site.register(ApplicationWebsite, ApplicationWebsiteAdmin)
admin.site.register(ApartmentPhoto, ApartmentPhotoAdmin)
admin.site.register(BuildingPhoto, BuildingPhotoAdmin)