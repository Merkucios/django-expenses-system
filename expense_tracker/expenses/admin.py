from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Category, Expense, Currency

admin.site.site_header = _("Учёт расходов")
admin.site.site_title = _("Панель администратора")
admin.site.index_title = _("Админ панель")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_category']
    search_fields = ['name']
    list_filter = ['parent_category']


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'currency', 'category', 'date', 'is_recurring']
    list_filter = ['user', 'category', 'date', 'is_recurring']
    search_fields = ['description']


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'symbol']
    search_fields = ['code', 'name']
