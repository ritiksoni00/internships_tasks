from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=10)
    weight = models.FloatField()
    price = models.IntegerField()
    created_at = models.DateField(auto_created=True)
    updated_at = models.DateField(auto_created=True)

    class Meta:
        db_table = 'prod'