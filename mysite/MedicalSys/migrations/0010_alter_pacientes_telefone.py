# Generated by Django 3.2.8 on 2021-10-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalSys', '0009_auto_20211011_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
    ]
