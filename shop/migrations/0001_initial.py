# Generated by Django 3.2.6 on 2021-09-04 09:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import shop.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('parental_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
            options={
                'verbose_name': 'subcategories',
            },
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_name', models.TextField(blank=True)),
                ('phone_number', models.TextField(blank=True, max_length=17, validators=[shop.validators.PhoneNumberValidator()])),
                ('cart', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.cart')),
            ],
        ),
        migrations.CreateModel(
            name='SellerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_name', models.TextField(blank=True)),
                ('phone_number', models.TextField(blank=True, max_length=17, validators=[shop.validators.PhoneNumberValidator()])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.sellerprofile')),
            ],
            options={
                'verbose_name': 'shops',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('categories', models.ManyToManyField(to='shop.Category')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
                ('tags', models.ManyToManyField(to='shop.Tag')),
            ],
            options={
                'verbose_name': 'products',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.TextField()),
                ('cvv', models.TextField()),
                ('date_expires', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField()),
                ('date_delivered', models.DateTimeField(blank=True, null=True)),
                ('date_handed', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('C', 'created'), ('D', 'delivering'), ('A', 'arrived'), ('H', 'handed')], max_length=1)),
                ('refund_requested', models.BooleanField(default=False)),
                ('refund_grunted', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customerprofile')),
                ('products', models.ManyToManyField(to='shop.Product')),
            ],
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='favorite_products',
            field=models.ManyToManyField(to='shop.Product'),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='shop.Product'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.TextField()),
                ('city', models.TextField()),
                ('street', models.TextField()),
                ('house', models.TextField()),
                ('corpus', models.TextField(blank=True)),
                ('floor', models.TextField(blank=True)),
                ('apartment', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customerprofile')),
            ],
            options={
                'verbose_name_plural': 'addresses',
            },
        ),
    ]
