from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, FormView

from apps.form import RegisterForm, ProfileForm
from apps.models import Product, ProductImage, User


class HomeTemplateView(ListView):
    model = Product
    template_name = 'apps/product/product-grid.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'apps/product/product-details.html'
    context_object_name = 'detail'


class ProductListView(ListView):
    model = Product
    template_name = 'apps/product/product-list.html'
    context_object_name = 'products'


class RegisterFormView(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'apps/auth/register.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return redirect('login')


class ProfileFormView(FormView):
    form_class = ProfileForm
    template_name = 'apps/auth/settings.html'

    def form_valid(self, form):
        if form.is_valid():
            User.objects.filter(pk=self.request.user.pk).update(**form.cleaned_data)
