# Generated by Django 2.0.6 on 2018-06-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
