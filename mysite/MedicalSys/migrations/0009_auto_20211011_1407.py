# Generated by Django 3.2.8 on 2021-10-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalSys', '0008_auto_20211011_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicos',
            name='data',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
