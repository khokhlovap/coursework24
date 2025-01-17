import io
import os
from django.http import HttpResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.conf import settings
from realty.models import InfoBuilding


def export_to_pdf(modeladmin, request, queryset):
    # Создаем поток для вывода PDF
    buffer = io.BytesIO()
    # Создаем PDF документ
    p = canvas.Canvas(buffer, pagesize=letter)
    # Устанавливаем заголовок для PDF
    p.setTitle("Информация о зданиях")

    font_path = os.path.join(settings.BASE_DIR,'realty/static/fonts/opensans.ttf')

    # Регистрируем шрифт, поддерживающий кириллицу
    pdfmetrics.registerFont(TTFont('Open Sans', font_path))
    p.setFont("Open Sans", 12)

    # Начальная позиция по Y
    y_position = 750

    # Добавляем заголовок
    p.drawString(100, y_position, "Информация о здании")
    y_position -= 20

    # Перебираем объекты из queryset и добавляем к документу
    for obj in queryset:
        p.drawString(100, y_position, f"Код дома: {obj.code_building}")
        y_position -= 15
        p.drawString(100, y_position, f"Город: {obj.city}")
        y_position -= 15
        p.drawString(100, y_position, f"Название улицы: {obj.street}")
        y_position -= 15
        p.drawString(100, y_position, f"№ дома: {obj.number_building}")
        y_position -= 30

        # Добавляем новую страницу, если позиция Y ниже определенного значения
        if y_position < 50:
            p.showPage()
            p.setFont("Open Sans", 12)
            y_position = 750

    # Закрываем PDF документ
    p.showPage()
    p.save()
    buffer.seek(0)

    # Возвращаем PDF в ответе
    return HttpResponse(buffer, content_type='application/pdf',
                        headers={'Content-Disposition': 'attachment; filename="building_info_export.pdf"'})
