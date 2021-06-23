# Generated by Django 3.1.1 on 2020-11-30 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='收货地址')),
                ('receiver', models.CharField(max_length=32, verbose_name='收货人')),
                ('receive_phone', models.CharField(max_length=32, verbose_name='联系电话')),
                ('postNumber', models.CharField(max_length=32, verbose_name='邮编')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=32, verbose_name='订单编号')),
                ('order_status', models.IntegerField(verbose_name='订单状态')),
                ('order_price', models.FloatField(verbose_name='订单总额')),
                ('order_date', models.DateTimeField(verbose_name='下单时间')),
                ('order_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.address', verbose_name='收货地址')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('nickname', models.CharField(max_length=32, verbose_name='昵称')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user/images', verbose_name='logo')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='联系电话')),
                ('contact_address', models.TextField(blank=True, null=True, verbose_name='联系地址')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(verbose_name='商品id')),
                ('product_name', models.CharField(max_length=32, verbose_name='商品名称')),
                ('product_price', models.FloatField(verbose_name='商品价格')),
                ('product_number', models.IntegerField(verbose_name='商品数量')),
                ('total_price', models.FloatField(verbose_name='商品总价')),
                ('shop_id', models.IntegerField(verbose_name='店铺id')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.order', verbose_name='所属订单')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='订单用户'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(verbose_name='商品id')),
                ('product_name', models.CharField(max_length=32, verbose_name='商品名称')),
                ('product_price', models.FloatField(verbose_name='商品价格')),
                ('product_number', models.IntegerField(verbose_name='商品数量')),
                ('total_price', models.FloatField(verbose_name='商品总价')),
                ('shop_id', models.IntegerField(verbose_name='店铺id')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.cart', verbose_name='所属购物车')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='订单用户'),
        ),
        migrations.AddField(
            model_name='address',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='用户ID'),
        ),
    ]