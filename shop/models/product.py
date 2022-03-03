from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, validate_image_file_extension
from shop.validators import validate_model_file_extensions
from statistics import mean


class Shop(models.Model):
    """
    Магазин

    Attributes:
        name            название магазина
        description     описание магазина
        rating          рейтинг магазина (float от 0 до 10)
        seller          профиль продавца
    """
    name = models.TextField(verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    seller = models.ForeignKey('SellerProfile', on_delete=models.CASCADE, verbose_name="Продавец")
    cover = models.FileField(
        verbose_name="Обложка магазина",
        blank=True, null=True,
        upload_to='static/shop_covers',
        validators=[validate_image_file_extension]
    )

    @property
    def rating(self):
        product_ratings = [product.rating for product in self.product_set.all() if product.rating is not None]
        if len(product_ratings) > 0:
            return mean(product_ratings)
        return None

    class Meta:
        verbose_name = 'shops'

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    Тег для выявления связей между товарами

    Attributes:
        name    название тега
    """
    name = models.TextField()  # TODO: добавить валидацию на отсутсвие пробелов

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Категория товара

    Attributes:
        name                название категории
        description         описание категории
        parental_category   id родительской категории
    """
    name = models.TextField()
    description = models.TextField(blank=True)
    parental_category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        blank=True, null=True,
        verbose_name="Родительская категория"
    )
    icon = models.FileField(
        blank=True,
        null=True,
        upload_to='static/category_icons',
        validators=[validate_image_file_extension],
        verbose_name="Иконка категории"
    )

    class Meta:
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Товар в магазине

    Attributes:
        name            наименование продукта
        description     описание
        price           цена
        shop            id мазазина продукта
        tags            теги
        categories      категории
    """
    name = models.TextField()
    description = models.TextField(blank=True)
    price = models.FloatField(validators=[MinValueValidator(0)])
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)
    discount = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    main_photo = models.FileField(
        verbose_name="Главное фото",
        blank=True,
        null=True,
        upload_to='static/photos',
        validators=[validate_image_file_extension]
    )
    model = models.FileField(
        verbose_name="3D модель",
        blank=True,
        null=True,
        upload_to='static/models',
        validators=[validate_model_file_extensions]
    )

    class Meta:
        verbose_name = 'products'

    @property
    def rating(self):
        comment_ratings = [comment.rating for comment in self.comment_set.all() if comment.rating is not None]
        if len(comment_ratings) > 0:
            return mean(comment_ratings)
        return None

    @property
    def is_discount(self):
        if self.discount > 0:
            return True
        return False

    def __str__(self):
        return self.name


class Comment(models.Model):
    """
    Комментарий к товару

    Attributes:
        author      автор комментария
        content     текст комментария
        product     откомментированный товар
        rating      оценка товара
    """
    author = models.ForeignKey('CustomerProfile', on_delete=models.CASCADE)
    content = models.TextField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)], null=True, blank=True, default=None
    )
