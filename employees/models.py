from django.db import models

# Create your models here.
class employee(models.Model):
    First_name = models.CharField(max_length=15)
    Last_name = models.CharField(max_length=15)
    DOB = models.DateField(null=True)
    Phone_Number = models.IntegerField()
    Address = models.CharField(max_length=200)

    def __str__(self):
        return self.First_name