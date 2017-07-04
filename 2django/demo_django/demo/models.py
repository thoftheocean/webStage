#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Publisher(models.Model):
    name=models.CharField(max_length=30,verbose_name='名字')
    address = models.CharField(max_length=50,verbose_name='地址')
    city = models.CharField(max_length=60,verbose_name='城市')
    state_province = models.CharField(max_length=30,verbose_name='省份')
    country = models.CharField(max_length=50,verbose_name='国家')
    website = models.URLField(verbose_name='网址')

    #定义显示名
    class Meta:
        verbose_name='出版商'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return self.name


class AuthorDetail(models.Model):
    sex=models.BooleanField(max_length=1,choices=((0,'男'),(1,'女'),))
    email=models.EmailField()
    address=models.CharField(max_length=50)
    birthday=models.DateField()
    author=models.OneToOneField(Author)

    class Meta:
        verbose_name = '作者详情'
        verbose_name_plural = verbose_name



class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10)

    class Meta:
        verbose_name = '书'
        verbose_name_plural = verbose_name


