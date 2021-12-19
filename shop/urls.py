"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from product.views import products_list, ProductDetailsView, ProductsListView, CreateProductView, UpdateProductView, \
    DeleteProductView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('products/', products_list, name='products_list')
    path('products/', ProductsListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='product-details'),
    path('products/create/', CreateProductView.as_view(), name='create-product'),
    path('products/update/<int:pk>/', UpdateProductView.as_view(), name='update-product'),
    path('products/delete/<int:pk>/', DeleteProductView.as_view(), name='delete-product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
