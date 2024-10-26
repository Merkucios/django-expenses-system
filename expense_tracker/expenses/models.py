from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name="Код валюты")
    name = models.CharField(max_length=50, verbose_name="Название валюты")
    symbol = models.CharField(max_length=5, blank=True, verbose_name="Символ валюты")

    def __str__(self):
        return f"{self.symbol} {self.code}"

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название категории")
    description = models.TextField(blank=True, verbose_name="Описание категории")
    parent_category = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name="subcategories",
        verbose_name="Родительская категория"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    amount = models.DecimalField(
        max_digits=12, decimal_places=2, validators=[MinValueValidator(0)],
        verbose_name="Сумма"
    )
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, verbose_name="Валюта")
    description = models.TextField(blank=True, verbose_name="Описание")
    date = models.DateField(verbose_name="Дата")
    receipt = models.FileField(upload_to="receipts/", blank=True, null=True, verbose_name="Квитанция")
    is_recurring = models.BooleanField(default=False, verbose_name="Повторяющийся расход")

    def __str__(self):
        return f"{self.amount} {self.currency} - {self.category} ({self.date})"

    class Meta:
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"
        ordering = ['-date']
