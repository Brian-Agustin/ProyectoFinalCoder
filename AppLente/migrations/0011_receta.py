# Generated by Django 4.1.1 on 2022-10-01 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLente', '0010_delete_receta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='media')),
            ],
        ),
    ]
