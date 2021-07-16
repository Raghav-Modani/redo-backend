# Generated by Django 3.2 on 2021-07-15 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0008_auto_20210712_2102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='receivers_contact',
            new_name='contact_number',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='receivers_landmark',
            new_name='landmark',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='receivers_pincode',
            new_name='zipcode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='receivers_add',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='default', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='address2',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_list',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
