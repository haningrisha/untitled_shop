# Generated by Django 3.2.6 on 2021-09-10 09:19

from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210910_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='cart',
            field=models.OneToOneField(auto_created=True, default=shop.models.create_cart, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.cart'),
        ),
    ]
