from rest_framework import serializers
import shop.models as shop_models


class ShopSerializer(serializers.ModelSerializer):
    seller = serializers.HyperlinkedRelatedField(view_name='seller-detail', read_only=True)
    product_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail'
    )

    class Meta:
        model = shop_models.Shop
        fields = ['id', 'name', 'description', 'rating', 'seller', 'seller_id', 'product_set', 'cover']
        extra_kwargs = {
            'seller_id': {'read_only': False},
            'rating': {'read_only': True}
        }


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Tag
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    parental_category = serializers.HyperlinkedRelatedField(
        view_name='category-detail',
        read_only=False,
        many=False,
        required=False,
        queryset=shop_models.Category.objects.all()
    )
    category_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='category-detail'
    )

    class Meta:
        model = shop_models.Category
        fields = ['id', 'name', 'description', 'parental_category', 'category_set']


class ProductSerializer(serializers.ModelSerializer):
    shop = serializers.HyperlinkedRelatedField(view_name='shop-detail', read_only=True)
    tags = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=False,
        queryset=shop_models.Tag.objects.all(),
        view_name='tag-detail'
    )
    categories = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=False,
        queryset=shop_models.Category.objects.all(),
        view_name='category-detail'
    )
    shop_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = shop_models.Product
        fields = [
            'id', 'name', 'description', 'price', 'discount', 'rating', 'shop', 'tags', 'categories', 'shop_id',
            'main_photo', 'model'
        ]
        extra_kwargs = {'rating': {'read_only': True}}


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedIdentityField(view_name='customer-detail')
    product = serializers.HyperlinkedIdentityField(view_name='product-detail')
    product_id = serializers.IntegerField()

    class Meta:
        model = shop_models.Comment
        fields = ['author', 'content', 'product', 'product_id', 'rating']
