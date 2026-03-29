from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Category

def product_list(request):
    products = Product.objects.all()
    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'count': product.count,
            'is_active': product.is_active,
            'category_id': product.category.id,
            'category_name': product.category.name
        })
    return JsonResponse(data, safe= False)

def category_list(request):
    categories = Category.objects.all()
    data = []
    for category in categories:
        data.append({
            'id': category.id,
            'name': category.name
        })
    return JsonResponse(data, safe=False)

def product_detail(request, id):
    product = Product.objects.get(id = id)
    data = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'count': product.count,
        'is_active': product.is_active,
        'category_id': product.category.id,
        'category_name': product.category.name
    }

    return JsonResponse(data)

def category_detail(request, id):
    category = Category.objects.get(id = id)
    data = {
        'id': category.id,
        'name': category.name
    }

    return JsonResponse(data)

def product_list_by_category(request, id):
    products = Product.objects.filter(category_id = id)
    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'count': product.count,
            'is_active': product.is_active,
            'category_id': product.category.id,
            'category_name': product.category.name
        })

    return JsonResponse(data, safe=False)



