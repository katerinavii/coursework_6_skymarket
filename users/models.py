from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'
    choices = (
        (USER, USER),
        (ADMIN, ADMIN)
    )


class User(AbstractBaseUser):

    # Определяем поле для логина пользователя
    USERNAME_FIELD = 'email'

    # Список с полями, которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    # Для работы модели пользователя определяем менеджер объектов
    objects = UserManager()

    first_name = models.CharField(
        max_length=64,
        verbose_name="Имя",
        help_text="Введите имя"
    )

    last_name = models.CharField(
        max_length=64,
        verbose_name="Фамилия",
        help_text="Введите фамилию"
    )

    email = models.EmailField(
        "email address",
        unique=True,
        help_text="Укажите электронную почту"
    )

    phone = PhoneNumberField(
        verbose_name="Телефон для связи",
        help_text="Введите телефон для связи"
    )

    role = models.CharField(
        max_length=20,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name="Роль пользователя",
        help_text="Выберите роль пользователя"
    )

    is_active = models.BooleanField(
        verbose_name="Аккаунт активен",
        help_text="Укажите, активен ли аккаунт"
    )

    image = models.ImageField(
        upload_to="users_avatars/",
        verbose_name="Аватарка",
        help_text="Выберите фото для аватара",
        null=True,
        blank=True
    )

    # Необходимые параметры для корректной работы Django
    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN  #

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)
