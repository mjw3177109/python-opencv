from flask import Flask
app = Flask(__name__)
from flask import request
@app.route('/',methods=['GET', 'POST'])
def hello_world():
   print("@2")
   f = request.files.get("img")
   print(f,type(f))
   print(f.stream.read())
   with open("./34334.png","wb")as n:
      n.write(f.stream.read())
   return 'Hello World'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5060, debug=True)
