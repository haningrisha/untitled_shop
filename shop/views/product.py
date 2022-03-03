from rest_framework import generics, status
from rest_framework.response import Response

import shop.models as shop_models
import shop.serializers as shop_serializers
from rest_framework import permissions
import shop.permissions as my_permissions
from .mixins import CreateProductAPIView, ListCreateAPIViewWithChecker
from shop.services import is_user_shop_owner
import django_filters.rest_framework

from compilations.services import add_product_history


class ShopListView(generics.ListCreateAPIView):
    """
    View списка всех магазинов

    Permissions:
        READ    все
        CREATE  только продавцы
    """
    queryset = shop_models.Shop.objects.all()
    serializer_class = shop_serializers.ShopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, my_permissions.IsInSellersGroupOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = shop_serializers.ShopSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        seller = request.user.sellerprofile
        serializer.save(seller_id=seller.id)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ShopDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View конкретного мазина по id

    Permissions:
        READ    все
        EDIT    только продавец
    """
    queryset = shop_models.Shop.objects.all()
    serializer_class = shop_serializers.ShopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, my_permissions.IsShopSellerOrReadOnly]


class ProductListView(ListCreateAPIViewWithChecker):
    """
    View списка всех товаров

    Permissions:
        READ    все
        CREATE  только продавцы и только в свои магазины
    """
    queryset = shop_models.Product.objects.all()
    serializer_class = shop_serializers.ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, my_permissions.IsProductSellerOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'tags', 'price', 'categories']
    check_detail = "You can add product only to your shop"
    custom_checks = [is_user_shop_owner]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View конкретного товара по id

    Permissions:
        READ    все
        EDIT    только продавец
    """
    queryset = shop_models.Product.objects.all()
    serializer_class = shop_serializers.ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, my_permissions.IsProductSellerOrReadOnly]

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        user = request.user
        add_product_history(product, user)
        return super().get(request, *args, **kwargs)


class ShopProductListView(CreateProductAPIView):
    """
    View товаров конкретного магазина

    Permissions:
        READ    все
        CREATE  только продавцы
    """
    serializer_class = shop_serializers.ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, my_permissions.IsProductSellerOrReadOnly]

    def get_queryset(self):
        return shop_models.Product.objects.filter(shop_id=self.kwargs.get('pk'))


class TagListView(generics.ListCreateAPIView):
    """
    View списка всех тегов

    Permissions:
        READ    все
        CREATE  только продавцы
    """
    queryset = shop_models.Tag.objects.all()
    serializer_class = shop_serializers.TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, my_permissions.IsInSellersGroupOrReadOnly]


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View конкретного тега по id

    Permissions:
        READ    все
        EDIT    только администратор
    """
    queryset = shop_models.Tag.objects.all()
    serializer_class = shop_serializers.TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, my_permissions.IsAdminOrReadOnly]


class CategoryListView(generics.ListCreateAPIView):
    """
    View списка всех категорий

    Permissions:
        READ    все
        CREATE  только администратор
    """
    queryset = shop_models.Category.objects.all()
    serializer_class = shop_serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, my_permissions.IsAdminOrReadOnly]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View конкретной категорий по id

    Permissions:
        READ    все
        EDIT    только администратор
    """
    queryset = shop_models.Category.objects.all()
    serializer_class = shop_serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, my_permissions.IsAdminOrReadOnly]


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View конкретного комментария

    Permissions:
        READ    все
        EDIT    только автор
    """
    queryset = shop_models.Comment.objects.all()
    serializer_class = shop_serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, my_permissions.IsCommentAuthorOrReadOnly]


class CommentListView(generics.ListCreateAPIView):
    """
    View списка всех комментариев

    Permissions:
        READ    все
        CREATE  все авторизованные пользователи
    """
    queryset = shop_models.Comment.objects.all()
    serializer_class = shop_serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = shop_serializers.CommentSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        author = request.user.customerprofile
        serializer.save(author_id=author.id)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
