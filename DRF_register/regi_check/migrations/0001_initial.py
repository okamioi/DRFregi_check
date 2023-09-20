# Generated by Django 4.1 on 2023-06-06 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=32, verbose_name='电话号码')),
                ('jianshu', models.CharField(max_length=32, verbose_name='简书')),
                ('weibo', models.CharField(max_length=32, verbose_name='微博')),
                ('baidu', models.CharField(max_length=32, verbose_name='百度')),
                ('aiqiyi', models.CharField(max_length=32, verbose_name='爱奇艺')),
            ],
        ),
    ]
