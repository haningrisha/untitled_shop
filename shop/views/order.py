from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response

import shop.models as shop_models
import shop.serializers as shop_serializers
import shop.permissions as my_permissions


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View конкретной корзины по id

    Permissions:
        READ    только покупатель
        EDIT    только покупатель
    """
    queryset = shop_models.Cart.objects.all()
    serializer_class = shop_serializers.CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, my_permissions.IsCustomer]


class CartListView(generics.ListCreateAPIView):
    """
    View списка всех корзин

    Permissions:
        READ    только покупатель и только своя корзина
        CREATE  создается автоматически
    """
    queryset = shop_models.Cart.objects.all()
    serializer_class = shop_serializers.CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, my_permissions.IsInCustomersGroup]

    def get_queryset(self):
        if self.request.user.is_staff:
            return shop_models.Cart.objects.all()
        else:
            customer_profile = self.request.user.customerprofile
            return shop_models.Cart.objects.filter(customerprofile=customer_profile)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View конкретного заказа по id

    Permissions:
        READ    только покупатель
        EDIT    только покупатель
    """
    queryset = shop_models.Order.objects.all()
    serializer_class = shop_serializers.OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, my_permissions.IsCustomer]


class OrderListView(generics.ListCreateAPIView):
    """
    View списка всех заказов

    Permissions:
        READ    только покупатель и только свои заказы
        CREATE  только покупатели
    """
    queryset = shop_models.Order.objects.all()
    serializer_class = shop_serializers.OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, my_permissions.IsInCustomersGroup]

    def get_queryset(self):
        if self.request.user.is_staff:
            return shop_models.Order.objects.all()
        else:
            customer_profile = self.request.user.customerprofile
            return shop_models.Order.objects.filter(customerprofile=customer_profile)

    def create(self, request, *args, **kwargs):
        serializer = shop_serializers.OrderSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        customer = request.user.customerprofile
        serializer.save(customer_id=customer.id)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
