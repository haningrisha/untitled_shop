from rest_framework import serializers
import shop.models as shop_models


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.PaymentMethod
        fields = ['id', 'card_number', 'cvv', 'date_expires']
        extra_kwargs = {'cvv': {'write_only': True}}


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=False,
        queryset=shop_models.Product.objects.all(),
        view_name='product-detail'
    )

    class Meta:
        model = shop_models.Order
        exclude = ['customerprofile']
        extra_kwargs = {
            'date_created': {'read_only': True},
            'date_delivered': {'read_only': True},
            'date_handed': {'read_only': True},
            'status': {'read_only': True},
            'refund_grunted': {'read_only': True}
        }


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Address
        exclude = ['customer']


class CartSerializer(serializers.ModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=False,
        queryset=shop_models.Product.objects.all(),
        view_name='product-detail'
    )

    class Meta:
        model = shop_models.Cart
        fields = ['id', 'products']
