from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
import os
from .inventory import InventoryManager
from .models import Product
from .forms import ProductForm  # Ensure you have a ProductForm in forms.py

inventory_manager = InventoryManager()

def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
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
        form = ProductForm(request.POST, request.FILES, instance=product)
        image_filename = request.POST.get('image_filename')  # Get the image filename from the form
        if form.is_valid():
            if image_filename:  # If the user provided an image filename
                image_path = os.path.join(settings.MEDIA_ROOT, 'products', image_filename)
                if os.path.exists(image_path):  # Check if the file exists
                    product.image = f'products/{image_filename}'  # Update the image field
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory_app/edit_product.html', {'form': form, 'product': product})

def product_delete(request, pk):  # Changed from 'id' to 'pk'
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'inventory_app/product_confirm_delete.html', {'product': product})