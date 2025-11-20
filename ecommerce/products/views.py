from django.shortcuts import render
from .models import Product, Category

def add_product(request):
    category, created = Category.objects.get_or_create(
        name="Default Category"
    )
    
    Product.objects.create(
        name="Sample Product", 
        description="This is a sample product.",
        price=9.99,
        category=category
    )  
    return render(request, "products/add_prod.html")
def all_products(request):
    products = Product.objects.all()
    return render(request, "products/all_products.html", {"products": products}) 