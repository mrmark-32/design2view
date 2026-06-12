# shop/context_processors.py
from .models import NavItem

def global_navbar(request):
    return {
        # CRITICAL FIX: Only grab items where parent is NULL (None)
        'nav_items': NavItem.objects.filter(parent=None)
    }