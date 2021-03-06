# Generated by Django 3.2.6 on 2021-09-10 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210909_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='cart',
            field=models.OneToOneField(auto_created=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.cart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'pending'), ('C', 'created'), ('D', 'delivering'), ('A', 'arrived'), ('H', 'handed')], default='P', max_length=1),
        ),
    ]
