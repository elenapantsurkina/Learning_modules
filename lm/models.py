from django.conf import settings
from django.db import models


class Learning(models.Model):
    """Модель образовательный модуль."""

    name = models.CharField(max_length=50, verbose_name="Название модуля", help_text="Укажите название модуля")
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание модуля", help_text="Укажите описание модуля"
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "Образовательный модуль"
        verbose_name_plural = "Образовательные модули"

    def __str__(self):
        return self.name
