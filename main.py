#!flask/bin/python
from flask import Flask
import os,random
import json
from getImageFromDb import founder
images=[]
results=[]
mypath="/home/yusufnuh/ftp/files"
entries = os.listdir(mypath)
                                
app = Flask(__name__)
@app.route('/api/bitirme/images/all')

def getAll():
    random.shuffle(entries)
    for entry in entries:
        images.append(entry)
        if len(images) == 5:
            break
    jsonobject=json.dumps(images)
    images.clear()
    return jsonobject


@app.route('/api/bitirme/images')

def getSingle():
    
    if 'name' in request.args:
        name =request.args['name']
    else:
        return "Error: No name field provided. Please specify an name."
    
    for image in entries:
        if image == name:
            results.append[image]    
        else:
            return "Error!This file could not found!"
    
    jsonobject=json.dumps(image)
    
    return jsonobject

@app.route('/api/bitirme/objects')
 def getObject():
     
     return output

if __name__ == '__main__':
    app.run(host='46.101.154.46',port='5000', debug=True)
