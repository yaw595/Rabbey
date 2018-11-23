from django.contrib import admin
from .models import Category, Product, Review


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'product', 'souvenir']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'discount', 'stock', 'available', 'featured', 'souvenir', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at', 'featured']
    list_editable = ['price', 'discount', 'stock', 'available', 'featured']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'product', 'text', 'created_at', 'approved', 'featured']
    list_editable = ['approved', 'featured']


admin.site.register(Review, ReviewAdmin)
