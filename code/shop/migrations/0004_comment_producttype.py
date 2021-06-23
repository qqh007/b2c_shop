# Generated by Django 3.1.1 on 2020-12-01 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20201126_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=32, verbose_name='商品类型')),
                ('description', models.TextField(verbose_name='详细信息')),
                ('picture', models.ImageField(upload_to='shop/images', verbose_name='首页展示图')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='发布用户')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('create_time', models.DateTimeField(verbose_name='发布时间')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='所属产品')),
            ],
        ),
    ]