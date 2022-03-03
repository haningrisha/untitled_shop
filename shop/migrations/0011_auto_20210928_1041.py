# Generated by Django 3.2.6 on 2021-09-28 10:41

import django.core.validators
from django.db import migrations, models
import shop.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20210926_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='static/category_icons', validators=[django.core.validators.validate_image_file_extension], verbose_name='Иконка категории'),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='static/avatars', validators=[django.core.validators.validate_image_file_extension], verbose_name='Изображение профиля'),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_photo',
            field=models.FileField(blank=True, null=True, upload_to='static/photos', validators=[django.core.validators.validate_image_file_extension], verbose_name='Главное фото'),
        ),
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.FileField(blank=True, null=True, upload_to='static/models', validators=[shop.validators.validate_model_file_extensions], verbose_name='3D модель'),
        ),
        migrations.AlterField(
            model_name='sellerprofile',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='static/avatars', validators=[django.core.validators.validate_image_file_extension], verbose_name='Изображение профиля'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to='static/shop_covers', validators=[django.core.validators.validate_image_file_extension], verbose_name='Обложка магазина'),
        ),
    ]