# Generated by Django 4.1.1 on 2022-10-03 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLente', '0012_delete_receta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('imagefile', models.FileField(null=True, upload_to='images/', verbose_name='')),
            ],
        ),
    ]