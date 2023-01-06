from django.db import models

# Create your models here.

class Product(models.Model):
    product_id =  models.AutoField
    product_name = models.CharField(max_length=60)
    category = models.CharField(max_length = 50,default= "")
    sub_category  = models.CharField(max_length = 50,default= "")
    desc = models.CharField(max_length = 200)
    price = models.IntegerField(default = 0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to = "shopapp/images",default = "")


    # we add this method for showing in admin product name 
    def __str__(self):
        return self.product_name