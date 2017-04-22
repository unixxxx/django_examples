from django.shortcuts import render, get_object_or_404
from .models import(
    Category,
    Product
)
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    language = request.LANGUAGE_CODE
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, translations__language_code=language,translations__slug=category_slug)
    context = {
        'category': category, 
        'categories': categories, 
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product,
                    id=id,
                    translations__language_code=language,
                    translations__slug=slug,
                    available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)  
