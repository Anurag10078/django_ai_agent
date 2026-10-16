from django.contrib import admin
from .models import Product,Order,RefundRequest
# Register your models here. to show in admin page 



#customization for our admin model 
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','category','in_stock']
    
class OrderAdmin(admin.ModelAdmin):
    list_display=['user', 'product_name', 'amount' ,'status' , 'carrier','tracking_number']
    
class RefunRequestAdmin(admin.ModelAdmin):
    list_display = ['order','user','reason','status','created_at']
    
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(RefundRequest,RefunRequestAdmin)