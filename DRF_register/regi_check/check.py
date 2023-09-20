import aiohttp, asyncio,re,requests
import regi_check.serializer as seri

isreg={
        "phoneNum":None,
        "baidu":'-',
        "aiqiyi":'-',
        "jianshu":'-',
        "weibo":'-',
        
    }


class Spider:
    def __init__(self, phone_num, data_list,post_data):
        self.phone = phone_num
        self.data_list = data_list  #config
        self.post_data = post_data  #平台信息

    
    
    async def make_get(self, session, url, data, headers):
        async with session.get( url,  params=data, headers=headers) as resp:
            return await resp.text()
    
    async def make_post(self, session, url, data, headers):
        async with session.post( url,  data=data, headers=headers) as resp:
            return await resp.text()
        
#在payload中加上号码
    async def check_register(self, data_dict):
        
        if re.search(data_dict.get('name'), self.post_data):
            data_dict['payload'][data_dict.get('phone_parameter')] =''
            data_dict['payload'][data_dict.get('phone_parameter')] += self.phone
            isreg['phoneNum']=self.phone
            #发送请求后，根据得到的数据判断是否已经注册
            async with aiohttp.ClientSession() as session:
                if data_dict.get('type') == 'POST':
                    r = await self.make_post(session,
                                                url=data_dict.get('url'),
                                                
                                                data=data_dict.get('payload'),
                                                headers=data_dict.get('headers'))
                elif data_dict.get('type') == 'GET':
                    if data_dict.get('verify'):
                        r = await self.make_get(session,
                                                    url=data_dict.get('url'),
                                                
                                                    data=data_dict.get('payload'),
                                                    headers=data_dict.get('headers'))
                    else:
                        r = requests.get(url=data_dict.get('url'),
                                        params=data_dict.get('payload'),
                                        verify=False)
                        r = r.text
                # print(r)        
                #正则搜索是否有相关参数
                if re.search(data_dict.get('unused_text'), r):                    
                    isreg.update({data_dict.get('name'):'否'})
                elif re.search(data_dict.get('err_text'), r):                    
                    isreg.update({data_dict.get('name'):'-'})
                    isreg.update({'status':2})
                    pass
                elif re.search(data_dict.get('used_text'), r):                    
                    isreg.update({data_dict.get('name'):'是'})
                else :                
                    # isreg.update({data_dict.get('name'):'somethingwrong'})
                    pass
                # print(isreg)
                
            
    def run(self):
        seri.clear_dict_values(isreg)
        # print(isreg)
        tasks = [self.check_register(data_dict) for data_dict in self.data_list ]
        try:    
            asyncio.run(asyncio.wait(tasks))
        except RuntimeError as e:
            if str(e)=='Event loop is closed':
                pass
            else:
                raise