"""DRF_register URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from regi_check import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/regi_check/',views.checkview.as_view()),                      #平台注册查询 and 记录全部删除
    re_path('api/regi_check/(\d.+)',views.checkdetailview.as_view()),       #单条记录删除
    path('api/regi_check/test/',views.checktestview.as_view()),             
    path('api/regi_check/history/',views.checkhistoryview.as_view()),       #历史记录
    path('api/regi_check/history/export/',views.checkexportview.as_view()), #单条记录导出
]
