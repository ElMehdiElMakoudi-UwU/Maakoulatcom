from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# View to handle product creation
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect after successful product creation
    else:
        form = ProductForm()
    
    return render(request, 'create_product.html', {'form': form})

# View to display the list of products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
