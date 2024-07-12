from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

class websites(models.Model):
    id = models.AutoField(primary_key=True)

    store_type = models.CharField(max_length=200)
    store_title = models.CharField(max_length=200)
    store_logo = models.CharField(max_length=200)
    store_url = models.CharField(max_length=200)

    title_tag = models.CharField(max_length=200)
    title_class = models.CharField(max_length=200)
    title_content = models.CharField(max_length=200)

    price_tag = models.CharField(max_length=200)
    price_class = models.CharField(max_length=200)
    price_content = models.CharField(max_length=200)

    availability_tag = models.CharField(max_length=200)
    availability_class = models.CharField(max_length=200)
    availability_content = models.CharField(max_length=200)

    sku_tag = models.CharField(max_length=200)
    sku_class = models.CharField(max_length=200)
    sku_content = models.CharField(max_length=200)


    ratings_tag = models.CharField(max_length=200)
    ratings_class = models.CharField(max_length=200)
    ratings_content = models.CharField(max_length=200)

    nbr_ratings_tag = models.CharField(max_length=200)
    nbr_ratings_class = models.CharField(max_length=200)
    nbr_ratings_content = models.CharField(max_length=200)

    delivry_price = models.CharField(max_length=200)
    offre = models.CharField(max_length=200)
    sitemap = models.TextField(default='')





    
    


    