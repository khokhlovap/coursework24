from django.contrib import admin
from django.utils import timezone
from .models import InfoBuilding, Apartment, StatusApartment, RegularCustomers, Deal2, ApplicationWebsite, ApartmentPhoto
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from datetime import datetime
from simple_history.admin import SimpleHistoryAdmin
from import_export import resources

class ApartmentInline(admin.TabularInline): 
    model = Apartment
    extra = 1  # Количество пустых форм для добавления новых объектов
    
class InfoBuildingAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('formatted_code', 'city', 'street', 'number_building')
    list_filter = ('city', 'code_building',)
    list_display_links = ('city',)
    inlines = [ApartmentInline]  # Добавляем inline

    @admin.display(description='Код здания')  # Указываем описание для заголовка столбца
    def formatted_code(self, obj):
        return f'Код: {obj.code_building}'  # Форматируем вывод
    
class ApartmentPhotoInline(admin.TabularInline):
    model = ApartmentPhoto
    extra = 1  # Количество пустых форм для добавления новых объектов

class ApartmentResource(resources.ModelResource):
    class Meta:
        model = Apartment
        fields = ('number_rooms', 'number_floor', 'square', 'price', 'code_building', 'apartment_code')

    def dehydrate_square(self, obj):
        """Форматируем площадь с указанием единиц измерения - кв.м """
        return f'{obj.square} кв.м' 
    
    def dehydrate_price(self, apartment):
        """Форматируем цену с указанием валюты - рубли"""
        return f'{apartment.price:.2f} руб.'

class ApartmentAdmin(SimpleHistoryAdmin, ImportExportModelAdmin,  ExportActionMixin, admin.ModelAdmin):
    resource_class = ApartmentResource
    list_display = ('number_rooms', 'number_floor', 'square', 'price', 'code_building', 'building_info', 'apartment_code')
    list_filter = ('number_rooms', 'number_floor', 'code_building',)
    readonly_fields = ('square',)
    search_fields = ('apartment_code',)  
    raw_id_fields=('code_building',)
    inlines = [ApartmentPhotoInline]  # Добавляем inline

    def get_export_filename(self, *args, **kwargs):
        current_date = datetime.now().strftime('%d.%m.%Y') # Получаем текущую дату для добавления в имя файла
        return f'Apartments_export_{current_date}.csv'
    
    def get_export_queryset(self, request):
        """Экспортируем только записи, где количество комнат >= 2"""
        queryset = super().get_export_queryset(request)
        print(request)
        return queryset.filter(number_rooms__gte=2)
    

class ApartmentPhotoAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
     list_display = ('apartment', 'image', 'description')

class StatusApartmentAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('id_apartment', 'status_apartment', 'formatted_date_change', 'id_client')
    date_hierarchy = 'data_change'
    raw_id_fields=('id_client', 'id_apartment',)
    list_filter = ('status_apartment',)

    @admin.display(description='Дата изменения')
    def formatted_date_change(self, obj):
        return obj.data_change.strftime('%d.%m.%Y')

class RegularCustomersInline(admin.TabularInline):  
    model = Deal2
    extra = 1  # Количество пустых форм для добавления новых объектов

class RegularCustomersAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('id', 'name_client', 'surname_client', 'number_phone', 'email_client')
    search_fields = ('name_client', 'surname_client', 'id')  
    inlines = [RegularCustomersInline]

class Deal2Admin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('apartment', 'client', 'formatted_date_change')
    raw_id_fields=('client', 'apartment',)
    date_hierarchy = 'data_deal'
 
    @admin.display(description='Дата изменения')
    def formatted_date_change(self, obj):
        return obj.data_deal.strftime('%d.%m.%Y')

class ApplicationWebsiteResource(resources.ModelResource):
    class Meta:
        model = ApplicationWebsite
        fields = ('name_client', 'number_phone', 'status_application', 'date_create3')

    def dehydrate_status_application(self, application_website):
        """Изменяем статус при экспорте"""
        if application_website.status_application == 'accepted':
            return "Принято"
        else:
            return "Отклонено"
        
    def dehydrate_date_create3(self, application_website):
        # Изменяем формат даты на дд.мм.гг
        return application_website.date_create3.strftime('%d.%m.%y')

class ApplicationWebsiteAdmin(SimpleHistoryAdmin, ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    resource_class = ApplicationWebsiteResource
    list_display = ('formatted_date_change', 'name_client', 'number_phone', 'status_application')
    date_hierarchy = 'date_create3'
    readonly_fields = ('date_create3',)
    list_filter = ('status_application',)

    @admin.display(description='Дата создания заявки')
    def formatted_date_change(self, obj):
        return obj.date_create3.strftime('%d.%m.%Y')
    
    def get_export_filename(self, *args, **kwargs):
        current_date = datetime.now().strftime('%d.%m.%Y') # Получаем текущую дату для добавления в имя файла
        return f'ApplicationWebsite_export_{current_date}.csv'

admin.site.register(InfoBuilding, InfoBuildingAdmin)
admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(StatusApartment, StatusApartmentAdmin)
admin.site.register(RegularCustomers, RegularCustomersAdmin)
admin.site.register(Deal2, Deal2Admin)
admin.site.register(ApplicationWebsite, ApplicationWebsiteAdmin)
admin.site.register(ApartmentPhoto, ApartmentPhotoAdmin)