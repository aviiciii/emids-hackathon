# Generated by Django 4.1.3 on 2022-11-09 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_alter_appointment_date_alter_appointment_examination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='medicine',
            field=models.ManyToManyField(blank=True, to='db.medicine'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='scan',
            field=models.ManyToManyField(blank=True, to='db.scan'),
        ),
    ]