# Generated by Django 3.1.1 on 2020-12-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201204_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_shop',
            field=models.IntegerField(default=1, verbose_name='店铺id'),
            preserve_default=False,
        ),
    ]
