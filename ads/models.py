from django.db import models

from users.models import User


class Ad(models.Model):
    """ Описание модели объявления. """

    title = models.CharField(
        max_length=200,
        verbose_name='Название товара',
        help_text='Введите название товара'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена товара',
        help_text='Введите цену товара'
    )
    description = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name='Описание товара',
        help_text='Введите описание товара'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='ads',
        verbose_name='Автор объявления',
        help_text='Выберите автора объявления'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания объявления'
    )
    image = models.ImageField(
        upload_to='images/',
        verbose_name='Фото',
        help_text='Добавьте фото для объявления',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']


class Comment(models.Model):
    """ Описание модели комментария. """

    text = models.CharField(
        max_length=1000,
        verbose_name='Комментарий',
        help_text='Оставьте комментарий здесь'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',
        help_text='Выберите автора комментария'
    )
    ad = models.ForeignKey(
        Ad, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Объявление',
        help_text='Объявление, к которому относится комментарий'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания объявления'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']
