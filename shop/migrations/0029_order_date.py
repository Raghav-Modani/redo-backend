# Generated by Django 3.2 on 2022-01-11 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
