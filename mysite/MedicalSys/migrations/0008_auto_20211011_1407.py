# Generated by Django 3.2.8 on 2021-10-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalSys', '0007_auto_20211010_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicos',
            name='data',
            field=models.DateTimeField(verbose_name='11/10/21'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='data',
            field=models.DateTimeField(verbose_name='11/10/21'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='telefone',
            field=models.CharField(max_length=14),
        ),
    ]