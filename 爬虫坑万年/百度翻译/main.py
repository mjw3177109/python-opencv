import requests

url = 'https://fanyi.baidu.com/sug'

# 写入要翻译的内容
word = input('请输入翻译的内容：')

data = {
    'kw': word
}
header = {
    'content-length': str(len(word)),  # 分析接口每次传入的文本长度会变化，使用len函数
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'  # 自动解析传入的字符形式
}
# 请求服务器
res = requests.post(url, data=data, headers=header)
# res.join() 将对象序列化为一个字符串
rescon = res.json()['data']
# print(res.json()['data']) # 返回服务器结果,数组的形式
for i in rescon:
    print(i['k']+'\n' + i['v']);
