#!flask/bin/python
from flask import Flask
import os,random
import json
images=[]
mypath="/home/yusufnuh/ftp/files"
entries = os.listdir(mypath)
                                
app = Flask(__name__)
@app.route('/bitirme/api/images')

def index():
    random.shuffle(entries)
    for entry in entries:
        images.append(entry)
        if len(images) == 5:
            break
    jsonobject=json.dumps(images)
    images.clear()
    return jsonobject

if __name__ == '__main__':
    app.run(host='46.101.154.46',port='5000', debug=True)
