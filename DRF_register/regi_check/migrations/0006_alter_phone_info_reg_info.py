# Generated by Django 4.1 on 2023-06-13 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regi_check', '0005_alter_phone_info_reg_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone_info',
            name='reg_info',
            field=models.JSONField(default=None, max_length=200, verbose_name='注册信息'),
        ),
    ]
