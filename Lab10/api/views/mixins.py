from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework import status
from ..models import Product,Category
from ..serializers import ProductSerializer, CategorySerializer

class ProductListAPIView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class ProductDetailListAPIView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    lookup_url_kwarg = 'product_id'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, product_id):
        return self.retrieve(request, product_id)
    
    def put(self, request, product_id):
        return self.update(request, product_id)
    
    def delete(self, request, product_id):
        return self.destroy(request, product_id)