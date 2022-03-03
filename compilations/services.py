import compilations.models as compilations_models
from shop.models import Product
from django.contrib.auth.models import User, Group
from django.db.models import Count, QuerySet


def is_customer(user):
    if user.is_anonymous:
        return False
    customer_group, create = Group.objects.get_or_create(name='Customers')
    return customer_group in user.groups.all()


def add_product_history(product: Product, user: User):
    if not is_customer(user):
        return
    record = compilations_models.ProductHistory(product=product, customer=user.customerprofile)
    record.save()


def get_discount_compilation() -> QuerySet:
    return Product.objects.filter(discount__gt=0).order_by('-discount')


def get_popular_compilation() -> QuerySet:
    return Product.objects.all().annotate(total=Count('producthistory__product_id')).order_by('-total')[:10]


def get_personal_compilation(user: User) -> QuerySet:
    if not is_customer(user):
        return Product.objects.none()
    customer = user.customerprofile
    return Product.objects\
        .filter(producthistory__customer_id=customer.id)\
        .annotate(total=Count('producthistory__product_id'))\
        .order_by('-total')[:10]
