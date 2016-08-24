# -*- coding: utf-8 -*-
from django.db import models

def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])

class Gallery(models.Model):
	username = models.CharField(max_length=100)
	tag = models.CharField(max_length=100)
	thumb = models.ImageField(upload_to='gallerythumbs/%Y/%m/%d')

class Document(models.Model):
    docfile = models.ImageField(upload_to='documents/%Y/%m/%d')
    #tag = models.CharField(max_length=100, default="summer")
    gallery = models.ForeignKey(
        Gallery,
        on_delete=models.CASCADE
        , default='0000000', editable=False
    )

class Choice(models.Model):
	choice = models.TextField(max_length=100)

