# Generated by Django 4.1 on 2023-06-06 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regi_check', '0002_remove_phone_info_aiqiyi_remove_phone_info_baidu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone_info',
            name='reg_info',
            field=models.CharField(default=None, max_length=100, verbose_name='注册信息'),
        ),
    ]
