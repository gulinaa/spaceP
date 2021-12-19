from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from product.forms import ProductForm
from product.models import Product, ProductImage


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/products_list.html', context)


# class ProductsListView(View):
#     def get(self, request):
#         products = Product.objects.all()
#         context = {'products': products}
#         return render(request, 'product/products_list.html', context)


class ProductsListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/main.html'
    context_object_name = 'products'
    paginate_by = 12


class ProductDetailsView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product_details.html'
    context_object_name = 'product'



#TODO:Реализовать при помощи функции



class CreateProductView(CreateView):
    queryset = Product.objects.all()
    template_name = 'product/create_product.html'
    form_class = ProductForm

    def post(self, request, *args, **kwargs):
        self.object = None
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            for image in request.FILES.getlist('product_image'):
                print(image)
                ProductImage.objects.create(product=product, image=image)
            return redirect(product.get_absolute_url())
        return self.form_invalid(form)


class UpdateProductView(UpdateView):
    queryset = Product.objects.all()
    form_class = ProductForm
    template_name = 'product/update_product.html'
    context_object_name = 'product'


class DeleteProductView(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('product-list')



#CRUD(create, retrive,update,delete)
#TODO:Реализовать CRUD/авторазиция/реализовать проверку прав пользователя

#SSR-server side render
#CSR-client side render


# MVC(Model-View-Controller)
# model - models
# view- template
# controller - view

