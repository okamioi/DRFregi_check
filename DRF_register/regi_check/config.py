data_list = [
    {
        'name':'jianshu',
        'url':'https://www.jianshu.com/users/register',
        'type':'POST',
        'use_poxies':False,
        'verify': True,
        'used_text':'手机号已经被使用',
        'unused_text':'验证码无效或已过期，请重新发送验证码',
        'err_text':'验证码错误次数过多，请稍后重试',
        'phone_parameter':'user[mobile_number]',
        'headers':{
            'Cookie': r'_ga=GA1.2.474973489.1582110939; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221703debf89c2b7-001ea025eeea3a-6313f69-921600-1703debf89d3b2%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22http%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D8e8EJXFcUmUTLIqMc3IugYPgGWfgcqyRpYRnk1zJbJDgWRAe27JadkqXEj-ZDiyR%26ck%3D6260.2.10.346.314.198.318.2%26shh%3Dwww.baidu.com%26wd%3D%26eqid%3Df1c7ed810004d400000000065e54c78a%22%7D%2C%22%24device_id%22%3A%221703debf89c2b7-001ea025eeea3a-6313f69-921600-1703debf89d3b2%22%7D; locale=zh-CN; _gid=GA1.2.1861532545.1582614418; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1582197016,1582434345,1582434780,1582614418; _m7e_session_core=75cd5c190099f3268795149ab1d32889; read_mode=day; default_font=font2; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fcaptchas%2Fnew%3Ft%3D1582614867140-53b; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1582614934',
            'Referer': 'https://www.jianshu.com/sign_up',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        },
        'payload':{
            'utf8': r'%E2%9C%93',
            'authenticity_token':'eOXnQKWzuHKSrLZ5L9sSqAgpBxYvmMB93zaJfSuqARsAV939uN1OzbsKYFWAp+AsJGu3BH6PJaPI64zpFu+y0Q==',
            'user[nickname]': 'eOXnQKWzuH',
            'user[mobile_number_country_code]': 'CN',
            'user[mobile_number]': '',
            'oversea': 'false',
            'force_user_nonexist': 'true',
            'sms_code': '1111',
            'captcha[validation][challenge]': '1d70c63d6ce297a067b34888d6da832e',
            'captcha[validation][gt]': 'ec47641997d5292180681a247db3c92e',
            'captcha[validation][validate]':'',
            'captcha[validation][seccode]':'',
            'captcha[id]': '',
            'security_number': 'true',
            'user[password]':'ec47641997d5292180sdsd',
            'commit': '注册'
        }
    },
    {
        'name':'weibo',
        'url':'https://weibo.com/signup/v5/formcheck',
        'type':'GET',
        'use_poxies':False,
        'verify': True,
        'used_text':'err',
        'unused_text':'ok',
        'err_text':'error',
        'phone_parameter':'value',
        'headers':{
            'Cookie': 'SUB=_2AkMTfY4_f8NxqwJRmP4RzG3iaIxxyQnEieKlIX_kJRMxHRl-yT9kqn0btRB6OP2g0JRjeBwB5OgLLk2qXxsH7bP0DYwJ; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W566Bc9IOn.E7hH1kxalCY9; PC_TOKEN=57041f6044; _s_tentry=-; appkey=; Apache=4288890460803.5337.1685958629987; SINAGLOBAL=4288890460803.5337.1685958629987; ULV=1685958629988:1:1:1:4288890460803.5337.1685958629987:',
            'Referer': 'https://weibo.com/signup/signup.php',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        },
        'payload':{
            'type': 'mobilesea',
            'zone': '0086',
            'value': '',
            'from': '',
            '__rnd': '1582636504070'
        }
    },
    {
        'name':'baidu',
        'url':'https://passport.baidu.com/v2/?regphonecheck&phone=&isexchangeable=1',
        'type':'GET',
        'use_poxies':False,
        'verify': False,
        'used_text':'0',
        'unused_text':'110000',
        'err_text':'50000',

        
        'phone_parameter':'phone', 
        'headers':{
            'Cookie': 'HMACCOUNT_BFESS=99925BA551ED5FDA; BIDUPSID=ED20DA9418D2F834EC3AA617B0D76D35; PSTM=1650353100; H_WISE_SIDS=110085_132548_188746_204906_211986_212296_212739_213028_213348_214795_215730_216849_216942_219623_219942_219946_222624_223064_224045_224055_226006_226627_228650_229154_229905_229968_230241_230288_230930_231627_231904_231919_231979_232052_232250_232273_232551_232728_232777_232908_233088_233393_233463_233465_233518_233603_233720_233850_234044_234085_234310_234514_234521_234559_234688_234721_234797_234813_234830_234922_234927_234959_234980_235087_235191_235196_235200_235230_235259_235414_235439_235511_235534_235587_235774_235831_235969_235979_236048_236049_236104_236242_236325_236395_236514_236518_236521_236528_236537_236614_236837_236940_237136_237147_237221_237246_237253_237255_237347_237384_237401_237429_237448_237451_237525; ZFY=lZpaTR9av9YOMLc5KkRWZLSSl:BNPxuRX7mRq5ufuMAo:C; __bid_n=1844bcff3bdae655304207; FEID=v10-5d07ca782aa4139825b2c0f7affe93e8f50631b3; BAIDU_WISE_UID=wapp_1672637163807_604; __xaf_fpstarttimer__=1672838235452; __xaf_thstime__=1672838235600; __xaf_fptokentimer__=1672838235610; H_WISE_SIDS_BFESS=110085_132548_188746_204906_211986_212296_212739_213028_213348_214795_215730_216849_216942_219623_219942_219946_222624_223064_224045_224055_226006_226627_228650_229154_229905_229968_230241_230288_230930_231627_231904_231919_231979_232052_232250_232273_232551_232728_232777_232908_233088_233393_233463_233465_233518_233603_233720_233850_234044_234085_234310_234514_234521_234559_234688_234721_234797_234813_234830_234922_234927_234959_234980_235087_235191_235196_235200_235230_235259_235414_235439_235511_235534_235587_235774_235831_235969_235979_236048_236049_236104_236242_236325_236395_236514_236518_236521_236528_236537_236614_236837_236940_237136_237147_237221_237246_237253_237255_237347_237384_237401_237429_237448_237451_237525; FPTOKEN=QV+7Y9kqkC3gHcMy5Qlz1BNufz7vm+zO5TRsXoUWmyXD9eVy1AT7Fujuyp23EjJrIjDeVnP13rTgow2mMdI4izMwb5T8aU1OZJYZHWv9UsxUvc1UKuJ5XOhVvnjHEC74iqWjTXgl7lbM1Ch70v+Fy+7CyTdH2e4aZNF9TtbOhcPK/pJkJ19mXghM6T1HB/tB5iDy+fhHClOJeRd/mLMQnF77A2ScsRrS45E9sVkQdP0UV3pf0xC9jRbjK4qGf7k5Y5a8LS8Qu/Tj2mL4BXhbu2SOutv+B+BD9UwBDS2FcWMXkfwHT/VO9hcP34Nt0iM4EY6+6UhFMmsfQYVEd3xGfQP0k3HIRrxYbtku3O3vjwP5UV9CnH5cvHeo5UU//DWg99OYrSVpnGnlkuhmGtDyYA==|Sq2GGMBdopG9kyCR74pfbsgNzcwVlWocdyG25u4TUv0=|10|4921ab9a92acdc34c0609b02c1cf165a; HMTK=1; BA_HECTOR=ak018g210k210l212525a4531i7be2q1n; BAIDUID=C980B0659FD1A3B5F5444857979D7CE3:FG=1; BAIDUID_BFESS=C980B0659FD1A3B5F5444857979D7CE3:FG=1; BDORZ=FAE1F8CFA4E8841CC28A015FEAEE495D; H_PS_PSSID=38515_36560_38768_38580_38486_38681_38414_26350_38619',
            'Referer': 'https://passport.baidu.com/v2/?regphonecheck&phone=&isexchangeable=1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        },
        'payload':{
            "phone": '', 
            "isexchangeable": 1
        }
    },
    {
        'name':'aiqiyi',
        'url':'https://passport.iqiyi.com/apis/user/check_account.action',
        'type':'POST',
        'use_poxies':False,
        'verify': True,
        'used_text':'true}$',
        'unused_text':'false}$',
        'err_text':'imgtype":1}', 
        'phone_parameter':'account', 
        'headers':{
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Origin": "https://www.iqiyi.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://www.iqiyi.com/iframe/loginreg?ver=1&is_reg=1",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9"
        },
        'payload':{
            "account":'', 
            "agenttype":1
        }       
    },
]