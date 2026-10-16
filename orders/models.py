from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#we will give access of these data to our ai agent
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    category = models.CharField(max_length=100)
    in_stock = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
#django already gives us user model
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending","Pending"),
        ("dispached","Dispached"),
        ("delivered","Delivered"),
        ("cancalled","Cancalled"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="orders") #if the product got deleted then also order should reflect which product was ordered 
    product_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default="pending")
    carrier = models.CharField(max_length=100,blank=True)
    tracking_number = models.CharField(max_length=100,blank=True)
    delivery = models.TextField(blank=True)
    created_at = models.DateTimeField()#in real project we add autonow add = true
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"Order #{self.id} -> {self.product} ({self.status})" #it is for the string representation for the order model 


class RefundRequest(models.Model):
    STATUS_CHOICES = [
            ("pending","Pending"),
            ("approved","Approved"),
            ("denied","Denied"),
        ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name="refund_requests")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="refund_requests")
    reason = models.TextField()
    #get_status_display
    status = models.CharField( max_length=20,choices=STATUS_CHOICES,default='pending')
    created_at = models.DateTimeField()
    
    def __str__(self):
        return f"Refund for Order #{self.order.id} -> {self.status}"
    