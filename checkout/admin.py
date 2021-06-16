from django.contrib import admin
from .models import Order, OrderItem

class OrderItemAdminInline(admin.TabularInline):
	model = OrderItem
	readonly_fields = ('orderitem_total',)

class OrderAdmin(admin.ModelAdmin):
	inlines = (OrderItemAdminInline,)

	readonly_fields = ('order_number', 'date', 'tax_rate', 'order_total', 'grand_total', 'hue_cart', 'stripe_pid')
	fields = ('order_number', 'date', 'user_full_name', 'email', 'phone_number', 'billing_address','tax_rate', 'order_total', 'grand_total', 'hue_cart', 'stripe_pid')
	list_display = ('order_number', 'date', 'user_full_name', 'order_total', 'tax_rate', 'grand_total',)
	ordering = ('-date',)

admin.site.register(Order, OrderAdmin)

