# Generated by Django 3.2.8 on 2021-10-07 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=60)),
                ('Telefone', models.IntegerField(default=0)),
                ('Endereco', models.CharField(max_length=30)),
                ('Numero', models.IntegerField(default=0)),
                ('Cidade', models.CharField(max_length=30)),
                ('UF', models.CharField(max_length=2)),
                ('Pais', models.CharField(max_length=20)),
                ('Cep', models.IntegerField(default=0)),
                ('data', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
