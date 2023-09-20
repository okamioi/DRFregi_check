from django.db import models

class Phone_Info(models.Model):
    telephone=models.CharField( verbose_name='电话号码',max_length=32)
    reg_info=models.CharField( verbose_name='注册信息',max_length=200,default=None)
    check_time = models.CharField( verbose_name='查询时间',max_length=32,default=None)
    pass



# Create your models here.
