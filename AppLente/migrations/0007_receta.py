# Generated by Django 4.1.1 on 2022-10-01 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLente', '0006_alter_turno_dni_alter_turno_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='recetas')),
            ],
        ),
    ]
