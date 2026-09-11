from django.db import models

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField()
    items_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStPC76lP66TQBd8ed7bBW2U6PQONb1q8Sruccq7zcBUHg2rU7iMMPhJGc&s=10')

