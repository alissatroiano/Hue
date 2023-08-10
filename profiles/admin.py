from django.contrib import admin
from django.conf import settings
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	fields = ('user', 'default_phone_number',
              'default_postcode',  'default_street_address1',
              'default_street_address2', 'default_town_or_city',
              'default_county', 'default_country', 'avatar')
