# Generated by Django 2.0.5 on 2018-07-21 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=20)),
                ('fullname', models.CharField(max_length=64)),
                ('mobileno', models.CharField(blank=True, max_length=30)),
                ('pincode', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=200)),
                ('landmark', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('address_type', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('image', models.ImageField(null=True, upload_to='products')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('rating', models.IntegerField()),
                ('units', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='products')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snapdealapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobileno', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ordereditems',
            name='products',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='snapdealapp.Product'),
        ),
        migrations.AddField(
            model_name='ordereditems',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='snapdealapp.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
