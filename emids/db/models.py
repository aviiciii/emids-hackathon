from django.db import models


class Sex(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=6)

    def __str__(self):
        return self.name

class Bloodgroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=4)

    def __str__(self):
        return self.name


# Create your models here.
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    sex= models.ForeignKey(Sex, on_delete=models.CASCADE)
    age= models.CharField(max_length=100)
    blood_group = models.ForeignKey(Bloodgroup, on_delete=models.CASCADE)
    emergency_contact= models.CharField(max_length=12)
    

    def __str__(self):
        return self.name

