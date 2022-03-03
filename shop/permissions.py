from rest_framework import permissions
from django.contrib.auth.models import Group


def is_admin(user):
    return bool(user and user.is_staff)


class IsUserOrReadOnly(permissions.BasePermission):
    """
    Право на редактирование данных пользователя только самим пользователем
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the object user
        return obj.user == request.user


class IsAdminOrCreateOnly(permissions.BasePermission):
    """
    Право на редактирование данных пользователя только самим пользователем
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method == 'POST':
            return True

        # Write permissions are only allowed to the object user
        return bool(
            request.user and
            request.user.is_staff
        )


class IsShopSellerOrReadOnly(permissions.BasePermission):
    """
    Право редактировать магазин только хозяину магазина
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the seller
        sellers_group, create = Group.objects.get_or_create(name='Sellers')
        if is_admin(request.user):
            return True
        if sellers_group in request.user.groups.all():
            return obj.seller.user == request.user
        return False


class IsProductSellerOrReadOnly(permissions.BasePermission):
    """
    Право редактировать магазин только хозяину магазина
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the seller
        sellers_group, create = Group.objects.get_or_create(name='Sellers')
        if is_admin(request.user):
            return True
        elif sellers_group in request.user.groups.all():
            return obj.shop.seller.user == request.user
        return False


class IsCommentAuthorOrReadOnly(permissions.BasePermission):
    """
    Право редактировать комментарий только автору
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the seller
        customers_group, create = Group.objects.get_or_create(name='Customers')
        if is_admin(request.user):
            return True
        elif customers_group in request.user.groups.all():
            return obj.author.user == request.user
        return False


class IsCustomer(permissions.BasePermission):
    """
    Право доступа только клиенту
    """

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the seller
        customers_group, create = Group.objects.get_or_create(name='Customers')
        if is_admin(request.user):
            return True
        elif customers_group in request.user.groups.all():
            return obj.customerprofile.user == request.user
        return False


class IsInCustomersGroup(permissions.BasePermission):
    """
    Право доступа только клиентам
    """

    def has_permission(self, request, view):
        # Write permissions are only allowed to the seller
        customers_group, create = Group.objects.get_or_create(name='Customers')
        if customers_group in request.user.groups.all() or is_admin(request.user):
            return True
        return False


class IsInCustomersGroupOrReadOnly(permissions.BasePermission):
    """
    Право на запись только клиентам
    """

    def has_permission(self, request, view):
        # Safe methods are allowed to everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the seller
        customers_group, create = Group.objects.get_or_create(name='Customers')
        if customers_group in request.user.groups.all() or is_admin(request.user):
            return True
        return False


class IsInSellersGroupOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the seller
        sellers_group, create = Group.objects.get_or_create(name='Sellers')
        if sellers_group in request.user.groups.all() or is_admin(request.user):
            return True
        return False


class IsInSellersGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        # Write permissions are only allowed to the seller
        sellers_group, create = Group.objects.get_or_create(name='Sellers')
        if sellers_group in request.user.groups.all() or is_admin(request.user):
            return True
        return False


class IsCustomerOrCreateOnly(permissions.BasePermission):
    """
    Право редактировать магазин только хозяину магазина
    """

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the seller
        # Read permissions are allowed to any request,
        if request.method == 'POST':
            return True
        sellers_group, create = Group.objects.get_or_create(name='Customers')
        if sellers_group in request.user.groups.all() or is_admin(request.user):
            return obj.customerprofile.user == request.user
        return False


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Право редактировать только администаратору
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the admin
        return bool(request.user and request.user.is_staff)


class IsUser(permissions.BasePermission):
    """
    Право на доступ данных пользователя только самим пользователем
    """

    def has_object_permission(self, request, view, obj):
        # All permissions are only allowed to the object user
        return obj.user == request.user


class IsUserOrAdmin(permissions.BasePermission):
    """
    Право доступа только самим пользователем или администратором
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff
