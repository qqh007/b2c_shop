# Generated by Django 3.1.1 on 2020-11-25 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='storeId',
        ),
        migrations.AddField(
            model_name='product',
            name='shopId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.shop', verbose_name='商品店铺'),
        ),
    ]
