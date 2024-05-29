from django.contrib import admin
from .models import Category, Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=["id","product_name","product_description","product_price",'category']

# Registering product model on the admin panel 
admin.site.register(Product,ProductAdmin)
#===============Registering catagory===============

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','category_slug']

    


admin.site.register(Category,CategoryAdmin)


