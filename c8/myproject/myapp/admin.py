from django.contrib import admin

# Register your models here.
from myapp.models import Ebom, Product, Mbom,Additional_details_wrapper,additional_product_that_are_added
admin.site.register(Ebom)
admin.site.register(Product)
admin.site.register(Mbom)
admin.site.register(Additional_details_wrapper)
admin.site.register(additional_product_that_are_added)