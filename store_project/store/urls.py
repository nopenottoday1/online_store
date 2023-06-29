from django.urls import path 
from .views import product_list, product_detail, category_detail,save_order


urlpatterns = [
    path('store/', product_list, name="product_list_url"), 
    path('product/<int:id>/', product_detail, name="product_detail_url"),
    path('category/<int:id>/', category_detail, name="category_detail_url"), 
    path('save_order', save_order)
]