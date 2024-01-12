from django.db import models

# Model for Product
from django.contrib.auth.models import User
class Customer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    name=models.CharField(max_length=200)

 # Advanced level | can set multi address feature
    address=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')
 # Advanced level | can set multi phone feature
    phone=models.CharField(max_length=10)

    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    

