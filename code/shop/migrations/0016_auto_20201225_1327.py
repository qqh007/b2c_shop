# Generated by Django 3.1.1 on 2020-12-25 05:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20201225_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='sales',
            field=models.FloatField(default=0, verbose_name='营业额'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 25, 5, 27, 25, 460615, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 25, 5, 27, 25, 459616, tzinfo=utc), verbose_name='生成时间'),
        ),
    ]
