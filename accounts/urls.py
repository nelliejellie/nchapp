from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password-reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
]