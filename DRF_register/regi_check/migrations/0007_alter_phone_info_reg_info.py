# Generated by Django 4.1 on 2023-06-13 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regi_check', '0006_alter_phone_info_reg_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone_info',
            name='reg_info',
            field=models.CharField(default=None, max_length=200, verbose_name='注册信息'),
        ),
    ]
