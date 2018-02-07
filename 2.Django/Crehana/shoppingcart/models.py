# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    """Esta clase representa el modelo de Items."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    price = models.FloatField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Representación legible del Item."""
        return "{} {}".format(self.name, self.price)


class Cart(models.Model):
    """Esta clase representa la relación entre Usuario e Items."""
    Item = models.ForeignKey(Item, null=False, blank=False,
                             on_delete=models.CASCADE)
    User = models.ForeignKey(User, null=False, blank=False,
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Representación legible de la compra."""
        return "{} {}".format(self.Item.name, self.User.username)
