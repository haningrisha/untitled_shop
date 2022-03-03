import shop.models as shop_models


def is_user_shop_owner(request, serializer) -> bool:
    """
    Проверяет является ли владелец магазина текущим пользователем

    :param request: запрос
    :param serializer: валидный сериалайзер
    :return: является ли владелец магазина текущим пользователем
    """
    shop = shop_models.Shop.objects.get(pk=serializer.validated_data['shop_id'])
    return shop.seller.user == request.user
