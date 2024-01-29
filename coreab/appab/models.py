# from django.db import models
# from django.db import models
#
#
# # Create your models here.
# class Modal(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.TextField(verbose_name="Имя")
#     email = models.TextField(verbose_name="Почта")
#     number = models.TextField(verbose_name="Номер")
#     otziv = models.TextField(verbose_name="Отзыв")
#
#     class Meta:
#         verbose_name = 'Модель'
#         verbose_name_plural = 'Модель'
#
#     def __str__(self):
#         return self.otziv
#
#
# class Tovar(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.TextField(verbose_name="Имя")
#     opisanie = models.TextField(verbose_name="Описание")
#     price = models.TextField(verbose_name="Цена")
#     photo = models.ImageField(upload_to='images/', blank=True)
#
#     class Meta:
#         verbose_name = 'Товар'
#         verbose_name_plural = 'Товар'
#
#     def __str__(self):
#         return self.name
