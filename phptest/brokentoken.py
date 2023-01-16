from qiniu import Auth, put_file, etag
import qiniu.config
        # 需要填写你的 Access Key 和 Secret Key
access_key = "9RFUYJ66lmAGAg0ZaDVWPdoGMRfCgR0KqXnjaWYQ"
secret_key = "IWmSrn8wPHj14fqNuMZbn0JDl1xc0GrlgjO9oqB1"
        # 构建鉴权对象
q = Auth(access_key, secret_key)
        # 要上传的空间
bucket_name = 'yuanchengyanhuo'
        # 生成上传 Token，可以指定过期时间等
# token = q.upload_token(bucket_name, expires=5555553600)
# print(token)
#         return Response({'code': 0, 'msg': '获取', 'data': {'uptoken': token}})
# #生成上传 Token，可以指定过期时间等
# key="facess.jpg"
# token = q.upload_token(bucket_name, key, 3600)
#
# # #要上传文件的本地路径
# localfile = './face.jpg'
# ret, info = put_file(token, key, localfile, version='v2')
# print(info,ret)
# print("http://rhioataex.hn-bkt.clouddn.com/"+key)
# # assert ret['key'] == key
# # assert ret['hash'] == etag(localfile)




# 上传到七牛后保存的文件名
#key = 'demo.png'

# 生成上传 Token，可以指定过期时间等
#token = q.upload_token(bucket_name, key, 3600)

# 上传文件的本地路径（就是你文件存放在本地盘的什么位置）
# localfile = './cat.jpg'
base_url="http://rhioataex.hn-bkt.clouddn.com/face.jpg"
private_url = q.private_download_url(base_url, expires=520000)
print(private_url)

# ret, info = put_file(token, key, localfile)
# print(info)
# # print(info)结果显示：_ResponseInfo__response:<Response [200]>, exception:None, status_code:200, text_body:{"hash":"FjE0k8sYsNUeG0tpmZ0cS14IxAJE","key":"demo.png"}, req_id:DNYAAABiT9yZJoMW, x_log:X-Log
#
# # 拼接路径   qtsrimd9d.hn-bkt.clouddn.com这个是创建空间分配的测试域名
# image_file = 'http://qtsri9d.hn-bkt.clouddn.com/' + ret.get('key')
# print(image_file)   # http://qtsri9d.hn-bkt.clouddn.com/demo.png
