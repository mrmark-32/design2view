from django.contrib import admin
from .models import Category, NavItem, FabricType, FabricFeature, WhyChooseUsReason


# 1. Setup the Inline layout for Fabric Types
class FabricTypeInline(admin.TabularInline):
    model = FabricType
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [FabricTypeInline]



@admin.register(NavItem)
class NavItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_name', 'order', 'is_premium_highlight')
    list_editable = ('order', 'is_premium_highlight') # Allows editing ordering numbers quickly inside list view
    



class FabricFeatureInline(admin.TabularInline):
    model = FabricFeature
    extra = 1  # Gives you a blank row out-of-the-box to quickly add features

class WhyChooseUsReasonInline(admin.TabularInline):
    model = WhyChooseUsReason
    extra = 1

@admin.register(FabricType)
class FabricTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order')
    list_filter = ('category',)
    inlines = [FabricFeatureInline, WhyChooseUsReasonInline]