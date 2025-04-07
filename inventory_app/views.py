from django.shortcuts import render, get_object_or_404, redirect
from .inventory import InventoryManager
from .models import Product
from .forms import ProductForm  # Ensure you have a ProductForm in forms.py

inventory_manager = InventoryManager()

def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list view
    else:
        form = ProductForm()
    return render(request, 'inventory_app/product_form.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory_app/product_list.html', {'products': products})

def product_detail(request, pk):  # Changed from 'id' to 'pk'
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory_app/product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        price = request.POST['price']
        product_id = len(inventory_manager.products) + 1  # Simple ID generation
        inventory_manager.add_product(product_id, name, quantity, price)
        return redirect('product_list')
    return render(request, 'inventory_app/product_form.html')

def product_edit(request, pk):  # Changed from 'id' to 'pk'
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory_app/product_form.html', {'form': form, 'product': product})

def product_delete(request, pk):  # Changed from 'id' to 'pk'
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'inventory_app/product_confirm_delete.html', {'product': product})