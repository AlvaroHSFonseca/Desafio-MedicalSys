# Generated by Django 3.2.8 on 2021-10-10 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalSys', '0005_alter_pacientes_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='cep',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='data',
            field=models.DateTimeField(verbose_name='20211009'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='numero',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='telefone',
            field=models.CharField(max_length=11),
        ),
    ]