from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
	model = OrderItem
	readonly_fields = ('orderitem_total',)


class OrderAdmin(admin.ModelAdmin):
	inlines = (OrderItemAdminInline,)

	readonly_fields = ('order_number', 'date',
                       'special_discount', 'order_total',
                       'grand_total', 'original_cart', 'stripe_pid')

	fields = ('order_number', 'date', 'user_full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'special_discount',
              'order_total', 'grand_total', 'original_cart', 'stripe_pid', "profile")

	list_display =  ('order_number', 'date', 'user_full_name',
                    'order_total', 'special_discount',
                    'grand_total',)
	
	ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
