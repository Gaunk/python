# Generated by Django 3.1.7 on 2021-03-10 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20210310_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listharga',
            name='price',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
    ]
