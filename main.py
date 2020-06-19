#!flask/bin/python
from flask import Flask,request,send_file
import os,random
import json
from saveImageInfo import saveImageInfo2Db
from manageDb import getSimilarImages,getAllImage
#from getImageFromDb import founder
images=[]
results=[]
mypath="/home/yusufnuh/files"
#entries = os.listdir(mypath)

app = Flask(__name__)
app.config["DEBUG"] = True
@app.route('/api/bitirme/images/all',methods=['GET'])
def getAll():

#    random.shuffle(entries)
    entries = getAllImage()
    random.shuffle(entries)
    for entry in entries:
        frame={"name" : "null" , "url" : "null"}
        url = "http://138.197.195.224:5000/api/bitirme/images?name=" + entry
        frame.update({"name" : entry})
        frame.update({"url": url})
        images.append(frame)
        #if len(images) == 5:
           # break
    jsonobject=json.dumps(images)
    images.clear()
    return jsonobject

@app.route('/api/bitirme/images/get',methods=['GET'])
def getByImageName():

    if 'img' in request.args:
        img =request.args['img']
    else:
        return "Error: No e field provided. Please specify an name."
   
    result=getSimilarImages(img)
    for entry in result:
        frame={"name" : "null" , "url" : "null"}
        url = "http://138.197.195.224:5000/api/bitirme/images?name=" + entry
        frame.update({"name" : entry})
        frame.update({"url": url})
        images.append(frame)

    jsonobject=json.dumps(images)
    images.clear()

    return jsonobject


    
@app.route('/api/bitirme/images',methods=['GET'])
def getSingle():
    
    if 'name' in request.args:
        name =request.args['name']
    else:
        return "Error: No name field provided. Please specify an name."
    
    return send_file('/home/yusufnuh/files/'+name)


@app.route('/api/bitirme/saveImageInfo',methods=['GET'])
def saveImageInfo():
    
    if 'img' in request.args:
        img=request.args['img']
    else:
        return "Error: No img field provided. Please specify an img."
   
    results=saveImageInfo2Db(img)
    return results


if __name__ == '__main__':
    app.run(host='138.197.195.224',port='5000', debug=True)
