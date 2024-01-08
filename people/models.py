from django.db import models
from phone_field import PhoneField

NULLABLE = {"null": True, "blank": True}
# Create your models here.


class People:
    name = models.CharField(max_length=25, verbose_name="Имя")
    family = models.CharField(max_length=25, verbose_name="Фамилия")
    soname = models.CharField(max_length=25, verbose_name="Отчество", **NULLABLE)
    phone = models.CharField(max_length=10,verbose_name="Телефон", **NULLABLE)

    def __str__(self):
        return f"{self.name}({self.family}), {self.soname}, {self.phone}"

    class Meta:
        verbose_name = "Собственник"  # Настройка для наименования одного объекта
        verbose_name_plural = (
            "Собственники"  # Настройка для наименования набора объектов
        )
