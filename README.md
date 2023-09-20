# DRFregi_check
运行前在DRF_register/settings中的Databases中添加自己数据库的用户名密码数据库名
---
主要查询逻辑在在regi_check的check.py中
---
原理是向登录网页发送带有手机号的数据，根据返回的数据的不同判断注册情况，所以会出现同一号码多次查询之后出现稍后再试的情况
---
需要添加更多平台只需要在config.py中根据网页返回数据的结构编写payload和判断文本即可
---
