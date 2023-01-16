import requests, os

base_url = 'https://tieba.baidu.com/f?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
}
# 保存文件地址
dirname = './tieba/woman/'
if not os.path.exists(dirname):
    os.makedirs(dirname)
# len(对象)表示某个字符串或者数组的长度
# range函数表示 返回的是列表
# pn中表示的是页码，i为range定义的页码,从0-10,使用抓包，寻找规律
# key自定义关键词
key = 'JavaScript'
for i in range(0, 10):
    params = {
        'ie': 'utf-8',
        'kw': key,
        'pn': str(i * 50)
    }
    response = requests.get(base_url, headers=headers, params=params)
    print(response.text)
    with open(dirname + 'js第%s页.html' % (i+1), 'w', encoding='utf-8') as file:
        file.write(response.content.decode('utf-8'))
