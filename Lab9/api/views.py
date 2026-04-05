from .models import Product, Category
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CategorySerializer,ProductSerializer

class CategoryViewSet (viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail = True, methods = ['get'], url_path = 'products')
    def products(self, request, pk = None):
        queryset = Product.objects.filter(category = pk)
        serializer = ProductSerializer(queryset, many = True)
        return Response(serializer.data)


class ProductViewSet (viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



