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
    mobile = models.CharField(max_length=13, blank=True, null=True)
    sex= models.ForeignKey(Sex, on_delete=models.CASCADE)
    age= models.CharField(max_length=5)
    blood_group = models.ForeignKey(Bloodgroup, on_delete=models.CASCADE)
    emergency_contact= models.CharField(max_length=13, blank=True, null=True)
    drinking=models.BooleanField(default=False)
    smoking=models.BooleanField(default=False)
    past_history = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    speciality= models.CharField(max_length=100, blank=True, null=True)
    mobile= models.CharField(max_length=13)

    def __str__(self):
        return 'Dr.' + str(self.id)


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    examination = models.ForeignKey("Examination", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.patient.name + ' ' + self.doctor.name


class Medicine(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Scan(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField(blank=True, null=True)
    type=models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.id


class Examination(models.Model):
    id=models.AutoField(primary_key=True)
    chief_complaint=models.CharField(max_length=100, blank=True, null=True)
    present_illness=models.CharField(max_length=100, blank=True, null=True)
    diagnosis=models.CharField(max_length=100, blank=True, null=True)
    scan=models.ManyToManyField(Scan, blank=True)   
    medicine=models.ManyToManyField(Medicine, blank=True)

    def __str__(self):
        return f'{self.id}'

