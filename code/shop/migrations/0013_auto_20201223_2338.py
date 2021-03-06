# Generated by Django 3.1.1 on 2020-12-23 15:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20201223_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='end_time',
        ),
        migrations.AlterField(
            model_name='coupon',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 15, 38, 6, 5664, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 15, 38, 6, 5664, tzinfo=utc), verbose_name='生成时间'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='picture',
            field=models.ImageField(null=True, upload_to='shop/images', verbose_name='首页展示图'),
        ),
    ]
