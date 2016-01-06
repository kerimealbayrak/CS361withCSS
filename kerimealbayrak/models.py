from __future__ import unicode_literals

from django.db import models


class student (models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()



class teacher (models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    officedetails = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()




class course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    classroom = models.CharField(max_length=100)
    times = models.CharField(max_length=100)
    student = models.ManyToManyField(student) #many students can be assigned in a course.
    teacher = models.ForeignKey(teacher)   #only single teaacher can be assigned in a course.
