from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Product,Category
from ..serializers import ProductSerializer, CategorySerializer

class ProductListAPIView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many= True)
        return Response(serializer.data)
    
    def post(self, request): 
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        
class ProductDetailAPIView(APIView):
    def get_object(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None
        
    def get(self, request, product_id):
        product = self.get_object(product_id)
        if product != None:
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, product_id):
        product = self.get_object(product_id)
        if product != None:
            serializer = ProductSerializer(product, data = request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, product_id):
        product = self.get_object(product_id)
        if product != None:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
