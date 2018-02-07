# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateItemView, CreateCartView

urlpatterns = {
    url(r'^items/$', CreateItemView.as_view(), name="create"),
    url(r'^carts/$', CreateCartView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
