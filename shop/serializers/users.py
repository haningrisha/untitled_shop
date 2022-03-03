from rest_framework import serializers
from django.contrib.auth.models import User
from .mixins import CreateUserSerializer
import shop.models as shop_models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class CustomerProfileSerializer(CreateUserSerializer):
    user = UserSerializer()
    cart = serializers.HyperlinkedIdentityField(view_name='cart-detail')
    favorite_products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=False,
        queryset=shop_models.Product.objects.all(),
        view_name='product-detail',
        required=False
    )

    class Meta:
        model = shop_models.CustomerProfile
        fields = ['id', 'user', 'cart', 'second_name', 'phone_number', 'avatar', 'favorite_products']

    def create(self, validated_data):
        favorite_products = validated_data.pop("favorite_products")
        customer_profile = super().create(validated_data)
        customer_profile.favorite_products.set(favorite_products)
        customer_profile.save()
        return customer_profile


class SellerProfileSerializer(CreateUserSerializer):
    shop_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='shop-detail'
    )
    user = UserSerializer()

    class Meta:
        model = shop_models.SellerProfile
        fields = ['id', 'user', 'second_name', 'phone_number', 'avatar', 'shop_set']
