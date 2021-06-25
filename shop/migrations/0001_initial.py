# Generated by Django 3.1.7 on 2021-06-25 10:54

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0005_auto_20210619_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('stationary', (('pencil', 'pencil'), ('paper', 'Paper'), ('eraser', 'Eraser'), ('other', 'Other'))), ('Category2', (('vhs', 'VHS Tape'), ('dvd', 'DVD'), ('pencil', 'Pencil'), ('paper', 'Paper'), ('other', 'Other'))), ('vhs', 'VHS Tape'), ('dvd', 'DVD'), ('pencil', 'Pencil'), ('paper', 'Paper'), ('Other', 'Other')], default='green', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=40)),
                ('receivers_add', models.CharField(default='', max_length=500)),
                ('receivers_pincode', models.IntegerField(default=0)),
                ('receivers_landmark', models.CharField(default='', max_length=100)),
                ('receivers_contact', models.IntegerField()),
                ('total', models.IntegerField(null=True)),
                ('status', models.CharField(default='order noted', max_length=15)),
                ('order_list', models.CharField(default='placed', max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SUbCategory1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory1', models.CharField(default='', max_length=40)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='SUbCategory2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory2', models.CharField(default='', max_length=40)),
                ('subcategory1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.subcategory1')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.property')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('product_for', models.CharField(choices=[('men', 'MEN'), ('women', 'WOMEN'), ('boy', 'BOY'), ('girl', 'GIRL'), ('general', 'GENERAL')], default='general', max_length=7)),
                ('brand', models.CharField(max_length=50, null=True)),
                ('tags', models.CharField(blank=True, default='blanktag', max_length=500, null=True)),
                ('cod_available', models.BooleanField(default=False)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, default=60.0, null=True)),
                ('original_price', models.FloatField(default=60.0, null=True)),
                ('desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('pub_date', models.DateField(blank=True, null=True)),
                ('delivery_charge', models.FloatField(default=60.0)),
                ('image', models.ImageField(default='', upload_to=shop.models.get_uplaod_file_name)),
                ('image2', models.ImageField(blank=True, null=True, upload_to=shop.models.get_uplaod_file_name)),
                ('image3', models.ImageField(blank=True, null=True, upload_to=shop.models.get_uplaod_file_name)),
                ('subcategory2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.subcategory2')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.vendoraccount')),
            ],
        ),
    ]
