from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50, blank=True)

    def  __str__(self): #It's Django用「 __unicode__」1會失敗
        """
        :returns: name string
        """
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=3, decimal_places=0)
    comment = models.CharField(max_length=50, blank=True)
    is_spicy = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant)

    def  __str__(self):
        """
        :returns: name string
        """
        return self.name

    class Meta:

        """Meta: attribute, options"""

        ordering = ['price'] # 若某項特性是排序的優先選擇(如總會以price為優先序)，需重複使用objects.order_by('price')。可改使用Meta

