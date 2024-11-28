from django.contrib import admin
from django.utils import timezone
from .models import InfoBuilding, Apartment, StatusApartment, RegularCustomers, Deal2, ApplicationWebsite

class ApartmentInline(admin.TabularInline):  # или admin.StackedInline
    model = Apartment
    extra = 1  # Количество пустых форм для добавления новых объектов
    

class InfoBuildingAdmin(admin.ModelAdmin):
    list_display = ('formatted_code', 'city', 'street', 'number_building')
    list_filter = ('city',)
    list_display_links = ('city',)
    inlines = [ApartmentInline]  # Добавляем inline

    @admin.display(description='Код здания')  # Указываем описание для заголовка столбца
    def formatted_code(self, obj):
        return f'Код: {obj.code_building}'  # Форматируем вывод

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('number_rooms', 'number_floor', 'square', 'price', 'code_building', 'building_info', 'apartment_code')
    list_filter = ('number_rooms',)
    readonly_fields = ('square',)

class StatusApartmentAdmin(admin.ModelAdmin):
    list_display = ('id_apartment', 'status_apartment', 'formatted_date_change', 'id_client')
    date_hierarchy = 'data_change'
    
    def id_apartment_display(self, obj):
        return obj.id_apartment.__str__()
    id_apartment_display.short_description = 'Квартира'
    
    @admin.display(description='Дата изменения')
    def formatted_date_change(self, obj):
        return obj.data_change.strftime('%d.%m.%Y')
    

class RegularCustomersInline(admin.TabularInline):  
    model = Deal2
    extra = 1  # Количество пустых форм для добавления новых объектов
    raw_id_fields=('apartment',)
    

class RegularCustomersAdmin(admin.ModelAdmin):
    list_display = ('name_client', 'surname_client', 'number_phone', 'email_client')
    search_fields = ('name_client', 'surname_client')  
    inlines = [RegularCustomersInline]

    

class Deal2Admin(admin.ModelAdmin):
    list_display = ('apartment', 'client', 'formatted_date_change')
 
    @admin.display(description='Дата изменения')
    def formatted_date_change(self, obj):
        return obj.data_deal.strftime('%d.%m.%Y')

class ApplicationWebsiteAdmin(admin.ModelAdmin):
    list_display = ('formatted_date_change', 'name_client', 'number_phone', 'status_application')
    date_hierarchy = 'date_create3'
    readonly_fields = ('date_create3',)

    @admin.display(description='Дата создания заявки')
    def formatted_date_change(self, obj):
        return obj.date_create3.strftime('%d.%m.%Y')

admin.site.register(InfoBuilding, InfoBuildingAdmin)
admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(StatusApartment, StatusApartmentAdmin)
admin.site.register(RegularCustomers, RegularCustomersAdmin)
admin.site.register(Deal2, Deal2Admin)
admin.site.register(ApplicationWebsite, ApplicationWebsiteAdmin)
