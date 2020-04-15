import pymongo

def connection():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["db_bitirme"]
    mycollection = mydb["image_properties"]
    return mycollection

def save2Db (filename,detectedObject):
    mycollection=connection()
    jsondata = {}
    objectDict={}
    jsondata['_id'] = filename
    jsondata['objects'] = []
    for eachObjectName in detectedObject:
        value=detectedObject.count(eachObjectName)
        objectDict[eachObjectName]=value
    
    jsondata['objects'].append(objectDict)

    mycollection.insert_one(jsondata)


#def getSimilarImage():
    #mycollection=connection()
    #similarImages={}
    