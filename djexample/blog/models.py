# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.postgres.fields import JSONField


class Book(models.Model):
    """book model"""
    name = models.CharField('书籍名称', max_length=40, blank=True, default='')
    extra_data = JSONField('扩展数据', default={})
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍'
        
