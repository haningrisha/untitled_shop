from django.db import models


class ProductHistory(models.Model):
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    customer = models.ForeignKey('shop.CustomerProfile', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
