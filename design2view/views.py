from django.shortcuts import render, get_object_or_404
from shop.models import Category, NavItem, FabricType # <-- Double check FabricType is here!

def home_page(request):
    categories = Category.objects.all()
    nav_items = NavItem.objects.all()
    context = {
        'categories': categories,
        'nav_items': nav_items
    }
    return render(request, 'home.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    context = {'category': category}
    return render(request, 'shop/category_detail.html', context)

# CRITICAL: This must be flush against the left side of the file!
def fabric_detail(request, category_slug, fabric_id):
    category = get_object_or_404(Category, slug=category_slug)
    fabric = get_object_or_404(FabricType, id=fabric_id, category=category)
    context = {
        'category': category,
        'fabric': fabric,
    }
    return render(request, 'fabric_detail.html', context)