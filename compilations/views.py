from rest_framework.generics import ListAPIView
from shop.serializers import ProductSerializer
import compilations.services as services


class DiscountCompilationView(ListAPIView):
    """
    Подборка товаров со скидкой
    """
    serializer_class = ProductSerializer
    queryset = services.get_discount_compilation()


class PopularCompilationView(ListAPIView):
    """
    Подборка популярных товаров
    """
    serializer_class = ProductSerializer
    queryset = services.get_popular_compilation()


class PersonalCompilationView(ListAPIView):
    """
    Персональная подборка товаров
    """
    serializer_class = ProductSerializer

    def get_queryset(self):
        return services.get_personal_compilation(self.request.user)
