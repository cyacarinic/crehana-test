# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from shoppingcart.models import Item, Cart


class FilterUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.User = request.user
        obj.save()

    def get_queryset(self, request):
        # For Django < 1.6, override queryset instead of get_queryset
        qs = super(FilterUserAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(User=request.user)
        else:
            return qs


class CustomCart(FilterUserAdmin):
    fieldsets = (
        (None, {
            'fields': ('Item', ),
        }),
    )


admin.site.register(Item)
admin.site.register(Cart, CustomCart)
