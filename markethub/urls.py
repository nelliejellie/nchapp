from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import include 


router = routers.DefaultRouter()
router.register('users', views.UserViewset)
router.register('products', views.ProductViewset)
router.register('artisan', views.ArtisanViewset)

urlpatterns = [
    path('markethub',views.markethub, name='markethub'),
    path('product_form',views.product_form, name='product_form'),
    path('product/<int:product_id>',views.product_detail, name='detail'),
    path('product/search_product/',views.search_product, name='search_product'),
    path('api', include(router.urls)),
]