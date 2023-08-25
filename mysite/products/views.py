from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Product,ProductReview
from django.db.models import Q
from django.shortcuts import render, get_object_or_404,redirect
from .forms import ProductSearchForm,ProductReviewForm

def index(request):
    products = Product.objects.all()
    search_query = request.GET.get('search_query')
    
    if search_query:
        products = products.filter(Q(name__icontains=search_query))
    return render(request, 'products/product_list.html', {'products': products})

    # return HttpResponse("Hello, world. You're at the products index.")

def product_list(request):
    products = Product.objects.all()
    search_query = request.GET.get('search_query')
    
    if search_query:
        products = products.filter(Q(name__icontains=search_query))
    return render(request, 'products/product_list.html', {'products': products})

# def product_detail(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     return render(request, 'products/product_detail.html', {'product': product})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.productreview_set.all()

    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('products:product_detail', product_id=product_id)
    else:
        form = ProductReviewForm()
    return render(request, 'products/product_detail.html', {'product': product, 'reviews': reviews, 'form': form})
