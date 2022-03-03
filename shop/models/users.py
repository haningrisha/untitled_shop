from django.db import models
from shop.validators import PhoneNumberValidator
from django.core.validators import validate_image_file_extension
from django.contrib.auth.models import Group
from .order import create_cart


class UserProfile(models.Model):
    """
    Абстрактный профиль пользователя

    Attributes:
        user                пользователь ассоциированный с профилем покупателя
        second_name         отчество
        phone_number        номер телефона покупателя
    """
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, verbose_name="Имя пользователя")
    second_name = models.TextField(blank=True, verbose_name="Отчество")
    phone_number = models.TextField(
        validators=[PhoneNumberValidator()],
        max_length=17,
        blank=True,
        verbose_name="Номер телефона")
    avatar = models.FileField(
        blank=True, null=True,
        upload_to='static/avatars',
        validators=[validate_image_file_extension],
        verbose_name="Изображение профиля"
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if hasattr(self, 'groups'):
            for group_name in self.groups:
                group, created = Group.objects.get_or_create(name=group_name)
                group.user_set.add(self.user)
                group.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class CustomerProfile(UserProfile):
    """
    Профиль покупателя

    Attributes:
        cart                корзина покупателя
        favorite_products   избранные товары
        groups              группы пользователя
    """
    cart = models.OneToOneField(
        'Cart',
        on_delete=models.CASCADE,
        null=True,
        auto_created=True,
        default=create_cart,
        verbose_name="Корзина",
        related_name="customerprofile"
    )
    favorite_products = models.ManyToManyField('Product')
    groups = ['Customers']


class SellerProfile(UserProfile):
    """
    Профиль хозяина магазина

    Attributes:
        groups  группы пользователя
    """
    groups = ['Sellers']

    def __str__(self):
        return f"{self.user.username} {self.user.last_name}"
