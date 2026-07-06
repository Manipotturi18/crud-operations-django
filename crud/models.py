from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.IntegerField(unique=True)
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField(unique=True)
    emp_address = models.CharField(max_length=250)

    def __str__(self):
        return self.emp_name
