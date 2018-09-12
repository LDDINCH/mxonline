# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models

class CityDict(models.Model):
    name = models.CharField(max_length=20,verbose_name=u'城市名')
    desc = models.CharField(max_length=200,verbose_name=u'描述')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

class CourseOrg(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'机构名称')
    desc = models.TextField(verbose_name=u'机构描述')
    click = models.IntegerField(default=0, verbose_name=u'机构点击数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')
    image = models.ImageField(upload_to='org/%Y/%m',max_length=300,verbose_name=u'封面图')
    address = models.CharField(max_length=100,verbose_name=u'机构地址')
    city = models.ForeignKey(CityDict,verbose_name=u'所在城市')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')


    class Meta:
        verbose_name = "机构"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name=u'所属机构')
    name = models.CharField(max_length=20,verbose_name=u'教师名字')
    work_years = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=100,verbose_name=u'就职公司')
    work_position = models.CharField(max_length=50,verbose_name=u'工作职位')
    points = models.CharField(max_length=50,verbose_name=u'教学特点')
    click = models.IntegerField(default=0, verbose_name=u'机构点击数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click', 'fav_nums']
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click', 'fav_nums', 'add_time']

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

# Create your models here.
