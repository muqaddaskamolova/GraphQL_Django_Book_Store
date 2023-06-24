from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(DeliveryOptions)
admin.site.register(PaymentSelections)