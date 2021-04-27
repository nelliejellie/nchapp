from django.urls import path
from . import views

urlpatterns = [
    path('skillhub',views.skillhub, name='skillhub'),
    path('skillhub/carpenter/',views.carpenter, name='carpenter'),
    path('skillhub/barber/',views.barber, name='barber'),
    path('skillhub/painter/',views.painter, name='painter'),
    path('skillhub/photographer/',views.photographer, name='photographer'),
    path('skillhub/electrician/',views.electrician, name='electrician'),
    path('skillhub/beautician/',views.beautician, name='beautician'),
    path('skillhub/baker/',views.baker, name='baker'),
    path('skillhub/fashion_designer/',views.fashion_designer, name='fashion_designer'),
    path('skillhub/hair_dresser/',views.hair_dresser, name='hair_dresser'),
    path('skillhub/realtor/',views.realtor, name='realtor'),
    path('skillhub/pers_shop/',views.pers_shop, name='pers_shop'),
    path('skillhub/soft_dev/',views.soft_dev, name='soft_dev'),
    path('skillhub/<int:skill_id>/',views.skill_detail, name='skill_detail'),
    path('skillhub/skill_form/',views.artisan_form, name='skill_form'),
]