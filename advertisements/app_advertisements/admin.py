from django.contrib import admin
from .models import Advertisements # импортируем модель из models текущей папки
# Register your models here.

class AdvertisementsAdmin(admin.ModelAdmin): # наследуем класс ModelAsmin, потому что это админский файлик
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'auction'] # демонстрация модели, ее поля
    list_filter = ['price', 'auction']
    actions = ['make_auction_false','make_auction_true'] # кнопочки-действия
    fieldsets = (                     # смысловые блоки в добавлении обьявления
        ('Общее', {
            'fields': ('title', 'description')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse', 'wide']   # collapse - возможность показать/скрыть; wide - на всю ширину
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_true(self, request, queryset):
        queryset.update(auction=True)



admin.site.register(Advertisements, AdvertisementsAdmin) # регистрация модели
