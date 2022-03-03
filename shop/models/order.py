from django.db import models

STATUSES = (
    ('P', 'pending'),
    ('C', 'created'),
    ('D', 'delivering'),
    ('A', 'arrived'),
    ('H', 'handed')
)


class Cart(models.Model):
    """
    Корзина

    Attributes:
        products    Продукты в корзине
    """
    products = models.ManyToManyField('Product')


def create_cart() -> Cart:
    cart = Cart()
    cart.save()
    return cart


class Order(models.Model):
    """
    Заказ

    Attributes:
        customer            профиль покупателя
        products            продукты в заказе
        date_created        дата создания заказа
        date_delivered      дата достовки заказа
        date_handed         дата получения заказа
        status              статус заказа (STATUSES)
        refund_requested    отправлен ли запрос на возврат денег
        refund_grunted      возвращены ли деньги за заказ
    """
    customerprofile = models.ForeignKey('CustomerProfile', on_delete=models.CASCADE)
    products = models.ManyToManyField('Product')
    date_created = models.DateTimeField(auto_now=True)
    date_delivered = models.DateTimeField(null=True, blank=True)  # TODO: ge than created check
    date_handed = models.DateTimeField(null=True, blank=True)  # TODO: ge than created check
    status = models.CharField(choices=STATUSES, max_length=1, default='P')
    refund_requested = models.BooleanField(default=False)
    refund_grunted = models.BooleanField(default=False)


class Address(models.Model):
    """
    Адрес

    Attributes:
        customer    профиль покупателя
        country     страна
        city        город
        street      улица
        house       номер дома
        corpus      номер корпуса
        floor       этаж
        apartment   номер квартиры
    """
    customer = models.ForeignKey('CustomerProfile', on_delete=models.CASCADE)
    country = models.TextField()
    city = models.TextField()
    street = models.TextField()
    house = models.TextField()
    corpus = models.TextField(blank=True)
    floor = models.TextField(blank=True)
    apartment = models.TextField()

    class Meta:
        verbose_name_plural = 'addresses'


class PaymentMethod(models.Model):
    """
    Способ оплаты

    Attributes:
        customer        профиль покупателя
        card_number     номер карты
        cvv             код CVV
        date_expired    срок работы карты
    """
    customer = models.ForeignKey('CustomerProfile', on_delete=models.CASCADE)
    card_number = models.TextField()
    cvv = models.TextField()
    date_expires = models.DateField()
