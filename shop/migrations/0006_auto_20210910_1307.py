# Generated by Django 3.2.6 on 2021-09-10 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210910_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='rating',
        ),
    ]
