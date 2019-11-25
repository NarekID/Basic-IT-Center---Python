from . import views
from django.urls import path, include

app_name = 'products'

urlpatterns = [
    # path('', views.ProductList.as_view(), name="product_list"),
    path('', views.ProductList.as_view(), name="product_list"),
    path('<slug:category>/<slug:owner>/<slug:slug>', views.product_detail, name="product_detail"),
]