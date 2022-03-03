from rest_framework import generics
from rest_framework import permissions

import shop.models as shop_models
import shop.serializers as shop_serializers
import shop.permissions as my_permissions


class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View конкретного профиля покупателей

    Permissions:
        READ    только покупатель и администратор
        EDIT    только покупатель
    """
    queryset = shop_models.CustomerProfile.objects.all()
    serializer_class = shop_serializers.CustomerProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, my_permissions.IsUserOrAdmin]


class CustomerListView(generics.ListCreateAPIView):
    """
    View списка всех профилей покупателей
    Если пользователь customer, то передается его профиль

    Permissions:
        READ    только администратор
        CREATE  все
    """
    serializer_class = shop_serializers.CustomerProfileSerializer
    permission_classes = [permissions.IsAuthenticated, my_permissions.IsInCustomersGroup]

    def get_queryset(self):
        if self.request.user.is_staff:
            return shop_models.CustomerProfile.objects.all()
        return shop_models.CustomerProfile.objects.filter(user=self.request.user)


class SellerListView(generics.ListCreateAPIView):
    """
    View списка всех продавцов
    Если пользователь seller, то передается его профиль

    Permissions:
        READ    только администратор
        CREATE  все
    """
    serializer_class = shop_serializers.SellerProfileSerializer
    permission_classes = [permissions.IsAuthenticated, my_permissions.IsInSellersGroup]

    def get_queryset(self):
        if self.request.user.is_staff:
            return shop_models.SellerProfile.objects.all()
        return shop_models.SellerProfile.objects.filter(user=self.request.user)


class SellerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View конкретного продавца по id

    Permissions:
        READ    только сам продавец
        EDIT    только сам продавец
    """
    queryset = shop_models.SellerProfile.objects.all()
    serializer_class = shop_serializers.SellerProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, my_permissions.IsUserOrAdmin]
