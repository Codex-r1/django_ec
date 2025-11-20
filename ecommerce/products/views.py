from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def add_product(request):
    category, created = Category.objects.get_or_create(
        name="Electronics"
    )
    
    # Create a product
    Product.objects.create(
        name="Sample Product", 
        description="This is a sample product with detailed information.",
        price=9.99,
        category=category
    )  
    return render(request, "products/add_prod.html")

def all_products(request):
    products = Product.objects.all()
    return render(request, "products/all_products.html", {"products": products})
