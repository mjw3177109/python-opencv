import requests
import time
import hashlib
import random
import json

# 创建一个类
class translation:
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        # 输入要翻译的文字
        self.key = input('请输入要翻译的内容:')
    def fanyi(self):
        # 计算字符的长度,根据分析可知 中文字符占9个长度 英文占1个 使用编码后中文字符所占字符为3
        if len(self.key) <= len((self.key).encode('utf8')):
            strs = (len((self.key).encode('utf8')) - len(self.key))//2
            mstr = len(self.key) - strs
            keylen = 234 + mstr + strs * 9
            print('当前输入的内容的长度为:%s' % keylen)
        # 获取当前的时间 random.randint 生成一个0-10的随机数
        ts = str(int(time.time())*1000)
        lts = str(int(time.time())*1000) + str(random.randint(0, 10))
        # 获取sign的值 n.md5("fanyideskweb" + e + i + "Tbh5E8=q6U3EXe+&L[4c@")
        strs1 = 'fanyideskweb'+self.key+lts+'Tbh5E8=q6U3EXe+&L[4c@'
        # print(strs1)
        # 加密
        sign = hashlib.md5(strs1.encode('utf8')).hexdigest()
        # print(sign)
        header = {
            'Content-Length': str(keylen),
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-368708839@10.108.160.18; JSESSIONID=aaaL2DMAbpTgg8Qpc2xUw; OUTFOX_SEARCH_USER_ID_NCOO=1451460344.418452; ___rl__test__cookies=1561684330987',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OSX10_14_2) AppleWebKit/537.36(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        data = {
            'i': self.key,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': lts,  # 获取的时间戳和随机数组合
            'sign': sign,  # 加密后
            'lts': ts,  # 时间戳
            'bv': '75b5d8bae54495d5ccd243908d1f65d4',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        ress =requests.post(self.url, headers=header, data=data).text
        res =json.loads(ress)
        # print(res)
        # 输出结果
        results = res['translateResult'][0][0]['tgt']
        print(self.key+'的翻译结果为:%s' % results)
if __name__ == '__main__':
    translation().fanyi()

