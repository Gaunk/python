# Generated by Django 3.1.7 on 2021-03-10 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listharga',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
    ]
