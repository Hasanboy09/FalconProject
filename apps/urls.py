from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from apps.views import HomeTemplateView, ProductDetailView, ProductListView, RegisterFormView, ProfileFormView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='product-grid'),
    path('product-detail/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('product-list/', ProductListView.as_view(), name='product_list')
]

urlpatterns += [
    path('auth/login', LoginView.as_view(template_name='apps/auth/login.html'), name='login'),
    path('auth/logout', LogoutView.as_view(template_name='apps/auth/login.html'), name='logout'),
    path('auth/register', RegisterFormView.as_view(), name='register'),
    path('auth/settings', ProfileFormView.as_view(), name='settings'),
]
