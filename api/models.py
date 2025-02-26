from django.db import models

# Create your models here.
class Student:
    def __init__(self, name, student_id, course, year):
        self.name = name
        self.student_id = student_id
        self.course = course
        self.year = year

