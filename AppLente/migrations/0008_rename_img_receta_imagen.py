# Generated by Django 4.1.1 on 2022-10-01 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppLente', '0007_receta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receta',
            old_name='img',
            new_name='imagen',
        ),
    ]
