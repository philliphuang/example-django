from django.db import models
from django.contrib.auth.models import User

"""creates model for each service able to be added to carts"""
class Cart_Item(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
"""creates model for customer linking Users to their 'carts' of items """
class Customer(models.Model):
    user = models.OneToOneField(User)
    cart = models.ManyToManyField(Cart_Item, blank=True)
    # TODO search_history = models.
    # TODO add more fields to extend auth.User
    
    def __str__(self):
        return self.user.username