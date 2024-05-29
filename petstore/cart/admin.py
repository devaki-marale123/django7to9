from django.contrib import admin
from .models import OrderItem, Orders

class OrderIteminline(admin.TabularInline):
    model=OrderItem
    




# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display: ["order_id","user","first_name","last_name","address_line_1","address_line_2",
    "city","state","phoneno"]
    inlines=[OrderIteminline]

admin.site.register(Orders,OrderAdmin)    

admin.site.register(OrderItem)

