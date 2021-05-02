from django.urls import path
from . import views



urlpatterns = [
    path('',views.index, name='index'),
    path('post/<int:detail_id>/<slug:post>/',views.post_detail, name='blog_detail'),
    path('vacancies/',views.vacancies, name='vacancies'),
    # path('post/<int:detail_id>/<slug:post>/',views.post_detail, name='blog_detail'),
]