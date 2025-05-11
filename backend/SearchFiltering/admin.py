from django.contrib import admin
from unfold.admin import ModelAdmin
from simple_history.admin import SimpleHistoryAdmin
from .models import Product , Category , Review

class UnfoldHistoryAdmin(SimpleHistoryAdmin , ModelAdmin):
    """Unfold + SimpleHistory combo admin"""
    pass


@admin.register(Product)
class ProductAdmin(UnfoldHistoryAdmin):
    list_display = ('title','price', 'size', 'color' , 'is_active' , 'created_at')
    list_filter = ("created_at", "is_active")
    search_fields = ("title", "color")
    ordering = ("-created_at",)
    
    
@admin.register(Category)
class CategoryAdmin(UnfoldHistoryAdmin):
    pass
    


@admin.register(Review)
class CategoryAdmin(UnfoldHistoryAdmin):
    pass
    
