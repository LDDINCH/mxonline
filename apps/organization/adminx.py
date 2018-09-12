# _*_ encoding:utf-8 _*_
__author__ = "ludada"
__date__ = "2018/8/16 10:37"
import xadmin

from .models import CityDict, CourseOrg, Teacher

class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']

class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click', 'fav_time', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click', 'fav_time', 'address', 'city']
    list_filter = ['name', 'desc', 'click', 'fav_time', 'address', 'city__name', 'add_time']

class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click', 'fav_nums',
                    'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click', 'fav_nums']
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click', 'fav_nums',
                   'add_time']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)

