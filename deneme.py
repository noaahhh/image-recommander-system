import pymongo
    
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["db_bitirme"]
mycollection = mydb["image_properties"]
 
detectedObject=['car','car','person','person','person']
jsondata = {}
jsondata['objects'] = []
for eachObjectName in detectedObject:
    objectDict={}
    value=detectedObject.count(eachObjectName)
    objectDict['name']=eachObjectName
    objectDict['count']=value
    if objectDict not in jsondata['objects']:
        jsondata['objects'].append(objectDict)
    

print(jsondata)
#mycollection.insert_one(jsondata)
