from qiniu import Auth, put_file, etag
import qiniu.config
import time
# access_key = 'Access_Key'
# secret_key = 'Secret_Key'
# q = Auth(access_key, secret_key)
# bucket_name = 'Bucket_Name'
key = 'face.jpg'
#上传文件到存储后， 存储服务将文件名和文件大小回调给业务服务器。
# policy={
#  'callbackUrl':'http://your.domain.com/callback.php',
#  'callbackBody':'filename=$(fname)&filesize=$(fsize)'
#  }

# token = q.upload_token(bucket_name, key, 3600, policy)
token="9RFUYJ66lmAGAg0ZaDVWPdoGMRfCgR0KqXnjaWYQ:1-mmV_uH5KzKOILltQOlxpWNqI4=:eyJzY29wZSI6Inl1YW5jaGVuZ3lhbmh1byIsImRlYWRsaW5lIjoxNjYyMDM1Njk4fQ=="
localfile = './face.jpg'
# print(time.time())
ret, info = put_file(token, key, localfile, version='v2')
print(info)
print(ret)
#http://rhioataex.hn-bkt.clouddn.com/face.jpg?token=9RFUYJ66lmAGAg0ZaDVWPdoGMRfCgR0KqXnjaWYQ:FuXFT_VxDEeKB8z6k-xPdT_cGM8f