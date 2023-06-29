from django.db import models

class Product(models.Model): 
    title=models.CharField(max_length=150, db_index=True)
    info=models.TextField(blank=True)
    price=models.IntegerField()
    categories=models.ManyToManyField("Category", blank=True, related_name="products")
    image= models.ImageField(upload_to="images/", default="images/default_picture.png")

    def __str__(self) -> str:
        return self.title


class Category(models.Model): 
    title=models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.title

class Order(models.Model): 
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    product= models.ForeignKey(Product, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.name