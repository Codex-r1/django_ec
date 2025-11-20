from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('add/', views.add_product, name="add_product"),
    path('all/', views.all_products, name="all_products"),
]