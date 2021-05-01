from django.urls import path
from . import views

urlpatterns = [
    path('markethub',views.markethub, name='markethub'),
    path('product_form',views.product_form, name='product_form'),
    path('product/<int:product_id>',views.product_detail, name='detail'),
    path('product/search_product/',views.search_product, name='search_product'),
]