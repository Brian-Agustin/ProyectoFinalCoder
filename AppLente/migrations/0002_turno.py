# Generated by Django 4.1 on 2022-09-05 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('dni', models.IntegerField()),
                ('fecha', models.CharField(max_length=50)),
            ],
        ),
    ]