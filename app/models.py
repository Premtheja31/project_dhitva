from django.db import models

# Create your models here.
class DataStorage(models.Model):
    name=models.CharField(max_length=100)
    tenth_marks=models.DecimalField(max_digits=4,decimal_places=2)
    inter_marks=models.PositiveIntegerField()
    degree_marks=models.DecimalField(max_digits=4,decimal_places=2)
    mobile=models.BigIntegerField(unique=True)
    mail=models.EmailField(max_length=254,unique=True)
    skills=models.CharField(max_length=200)
    work_experience=models.PositiveSmallIntegerField()
    def __str__(self):
        return self.name