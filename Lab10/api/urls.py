from rest_framework.routers import DefaultRouter
from .tempview import ProductViewSet, CategoryViewSet
from django.urls import path, include
from .views import fbv as fbv_views
from .views import cbv as cbv_views
from .views import mixins as mixins_views
from .views import generics as generics_views

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('fbv/products/', fbv_views.product_list),
    path('fbv/products/<int:product_id>/', fbv_views.product_detail_list),

    path('cbv/products/', cbv_views.ProductListAPIView.as_view()),
    path('cbv/products/<int:product_id>/', cbv_views.ProductDetailAPIView.as_view()),

    path('mixins/products/', mixins_views.ProductListAPIView.as_view()),
    path('mixins/products/<int:product_id>/', mixins_views.ProductDetailListAPIView.as_view()),

    path('generics/products/', generics_views.ProductListAPIView.as_view()),
    path('generics/products/<int:product_id>/', generics_views.ProductDetailAPIView.as_view()),
    path('generics/categories/', generics_views.CategoryListAPIView.as_view()),
    path('generics/categories/<int:category_id>/', generics_views.CategoryDetailAPIView.as_view()),
    path('generics/categories/<int:category_id>/products/', generics_views.CategoryProductsAPIView.as_view()),
]