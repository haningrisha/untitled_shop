# Generated by Django 3.2.6 on 2021-09-25 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Изображение профиля'),
        ),
        migrations.AddField(
            model_name='sellerprofile',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Изображение профиля'),
        ),
    ]
