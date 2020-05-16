from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField("Name", max_length=100)
    grade = models.CharField("Grade", max_length=20)
    school = models.CharField("School", max_length=100)
    email = models.EmailField()
    userid = models.CharField("User Id", max_length=20)
    phone = models.CharField(max_length=20)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.name