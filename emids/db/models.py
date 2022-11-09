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
    drinking=models.BooleanField(default=False)
    smoking=models.BooleanField(default=False)
    past_history = models.CharField(maxlength=100)


    def __str__(self):
        return self.name

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    speciality= models.CharField(max_length=100)
    mobile= models.CharField(max_length=12)

    def __str__(self):
        return 'Dr.' + self.name

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    examination-= models.ForeignKey("Examination", on_delete=models.CASCADE)


    def __str__(self):
        return self.patient.name + ' ' + self.doctor.name




class Medicine(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)





class Scan(models.Models):
    id=models.AutoField(primary_key=True)
    date=models.DateField()
    type=models.CharField(max_length=100)
    
    def __str__(self):
        return self.id

class Examination(models.Models):
    id=models.AutoField(primary_key=True)
    scan=models.ForeignKey(Scan, on_delete=models.CASCADE)
    chief_complaint=models.CharField(max_length=100)
    present_illness=models.CharField(max_length=100)
    diagnosis=models.CharField(max_length=100)
    Prescription=models.ForeignKey(Prescription, on_delete=models.CASCADE)

    def __str__(self):
        return self.id



class Prescription(models.Model):
    id=models.AutoField(primary_key=True)
    appointment=models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medicine=models.ManyToManyField(Medicine)

    def __str__(self):
        return self.id









    