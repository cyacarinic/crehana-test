# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from django.shortcuts import render
from rest_framework import generics
from .serializers import ItemSerializer, CartSerializer
from .models import Item, Cart


class CreateItemView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class CreateCartView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
