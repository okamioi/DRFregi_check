# Generated by Django 4.1 on 2023-06-06 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regi_check', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone_info',
            name='aiqiyi',
        ),
        migrations.RemoveField(
            model_name='phone_info',
            name='baidu',
        ),
        migrations.RemoveField(
            model_name='phone_info',
            name='jianshu',
        ),
        migrations.RemoveField(
            model_name='phone_info',
            name='weibo',
        ),
        migrations.AddField(
            model_name='phone_info',
            name='reg_info',
            field=models.CharField(default=None, max_length=32, verbose_name='注册信息'),
        ),
    ]
