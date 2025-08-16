#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, MenuItem, Order, OrderItem

# Inline for showing OrderItems within the Order view in admin
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['menu_item'] # Use a raw ID field for easier selection of menu items
    extra = 1 # Number of extra forms to display

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'is_paid', 'total_price')
    list_filter = ('is_paid', 'created_at')
    search_fields = ('user__username', 'id')
    inlines = [OrderItemInline] # Add the inline for OrderItems

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'menu_item', 'quantity', 'price')
    list_filter = ('order__created_at',)
    search_fields = ('menu_item__name',)

