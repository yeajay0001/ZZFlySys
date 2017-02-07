from django.db import models

# Create your models here.
class OrderModel(models.Model):
    ResultID = models.IntegerField(primary_key=True)  
    
    MainID = models.CharField(max_length=30)
    MainOrderInputDate = models.CharField(max_length=30)
    MAWBNO = models.CharField(max_length=30)  
    OrderComp = models.CharField(max_length=30)
    OrderSubmitor = models.CharField(max_length=30)
    ShipperNameAndAddr = models.CharField(max_length=30)
    AirComp = models.CharField(max_length=30)
    
    def __str__(self):
        return self.userName