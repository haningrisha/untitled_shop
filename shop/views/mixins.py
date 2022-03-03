from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
import shop.serializers as shop_serializers
from rest_framework.exceptions import PermissionDenied


class CreateProductAPIView(ListCreateAPIView):
    def create(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'price': request.data.get('price'),
            'shop_id': request.data.get('shop_id', kwargs.get('pk'))
        }
        serializer = shop_serializers.ProductSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ListCreateAPIViewWithChecker(ListCreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if self._is_valid_by_checks(request, serializer):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        raise PermissionDenied(detail=self.check_detail)

    def _is_valid_by_checks(self, request, serializer):
        return all([check(request, serializer) for check in self.custom_checks])
