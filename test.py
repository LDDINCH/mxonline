# _*_ encoding:utf-8 _*_
__author__ = "ludada"
__date__ = "2018/9/3 21:55"
import random
a = [1,2]
b = ['a','b','c']
c = zip(a,b)
print(random.choice(a))
for d, e in c:
    print(d,e)
    print(random)
from fractions import Fraction
print(Fraction(1,3))
from time import strftime,localtime
print (strftime('%Y-%m-%d %H:%M:%S', localtime()))
from datetime import datetime
print(datetime.now())