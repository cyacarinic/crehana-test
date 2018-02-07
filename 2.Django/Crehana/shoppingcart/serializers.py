# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Item
from .models import Cart


class ItemSerializer(serializers.ModelSerializer):
    """Mapping del modelo en formato JSON."""

    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'created', 'updated')
        read_only_fields = ('created', 'updated')


class CartSerializer(serializers.ModelSerializer):
    """Mapping del modelo en formato JSON."""

    class Meta:
        model = Cart
        fields = ('id', 'Item', 'User', 'created')
        read_only_fields = ('created', None)
