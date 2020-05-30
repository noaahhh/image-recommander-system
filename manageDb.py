import pymongo

def connection(collectionName):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["db_bitirme"]
    mycollection = mydb[collectionName]
    return mycollection

def save2Db (filename,detectedObject):
    mycollection=connection("image_properties")
    jsondata = {}
    jsondata['_id'] = filename
    jsondata['objects'] = []
    for eachObjectName in detectedObject:
        objectDict={}
        value=detectedObject.count(eachObjectName)
        objectDict['name']=eachObjectName
        objectDict['count']=value
        if objectDict not in jsondata['objects']:
            jsondata['objects'].append(objectDict)
    

    result_object=mycollection.insert_one(jsondata)
    return result_object

def getSimilarImages(img):
    
    mycollection=connection("similar_images")
    doc=mycollection.find({"name":img})
    for key in doc:
        array=key["similar_images"]
    print(array)    
    return array

def getAllImage():
    array=[]
    mycollection=connection("similar_images")
    doc=mycollection.find({"similar_images": { "$exists" : 1, "$ne": [] } })
    for key in doc:
        array.append(key["name"])
    print(array)
    return array

