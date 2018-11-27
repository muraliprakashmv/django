from django.db import models

# Create your models here.


class student(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    address=models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta():
        db_table='student'

class teacher(models.Model):
    name = models.CharField(max_length=50)
    student=models.ForeignKey(student,on_delete=models.PROTECT)
    email=models.EmailField(max_length=50)
    city=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    is_active=models.BooleanField(default=True)

    class Meta():
        db_table='teacher'


class sgpg(models.Model):
    first_name=models.CharField(max_length=25)
    middle_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    gender=models.CharField(max_length=10)
    email_id=models.EmailField(max_length=50)
    phone1=models.CharField(max_length=15)
    phone2=models.CharField( max_length=15)
    parents_name=models.CharField(max_length=30)
    parents_phone=models.CharField(max_length=15)
    address=models.CharField(max_length=250)
    joining_date=models.CharField(max_length=50)
    deposit=models.CharField(max_length=8)
    rent=models.CharField(max_length=8)
    pending=models.CharField(max_length=8)
    is_active=models.BooleanField(default=True)

    class Meta():
        db_table='sgpg'
