# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.postgres.fields import JSONField

from djexample.djtools import widgets
from . import models


class CommonAdminMixin(admin.ModelAdmin):
    """Common Admin Mixin"""
    list_max_show_all = 20
    list_per_page = 20

    formfield_overrides = {
        JSONField: {'widget': widgets.JsonEditorWidget}
    }

    class Media:
        from django.conf import settings
        static_url = getattr(settings, 'STATIC_URL')

        css = {
            'all': (static_url + 'jsoneditor.min.css', )
        }
        js = (static_url + 'jsoneditor-minimalist.min.js', )


@admin.register(models.Book)
class BookAdmin(CommonAdminMixin):
    """docstring for BookAdmin"""
    list_display = ['id', 'name']
