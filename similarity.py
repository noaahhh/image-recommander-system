from sklearn.metrics.pairwise import cosine_similarity
import pymongo
from manageDb import connection
import copy

def first_Image_List_Generator(name,my_list,collection,namelist):
    mydoc=collection.find({"_id":name})
    for key  in mydoc:
        array= key["objects"]
        for y in array:
            namelist.append(y["name"])
            my_list.append(y["count"])

       # pirnt(namelist)
def similarityService():
    mycollection=connection("image_properties")
    mycollection2=connection("similar_images")
    a=[]
    b=[]
    images=[]
    names_1=[]
    names_2=[]
    tmp=[]
    similar=[]
    query=None


    image_names=mycollection.find({"_id"   :  {"$exists":1 }   },{"_id":1})
    for x in image_names:
#        print(x["_id"])
        images.append(x["_id"])
    
    image_names2=mycollection.find({"_id"   :  {"$exists":1 }   },{"_id":1})
    for x in image_names2:
#        print(x["_id"])
        query=copy.copy(x["_id"])
        print(query)

        first_Image_List_Generator(query,a,mycollection,names_1)
        tmp=copy.copy(a)
        print("names:"+str(names_1))
        print(a)
#       print("tmp" + str(tmp))

        for name in images:
            if name!=query:
                print(name)
                mydoc=mycollection.find({"_id":name})
                for key  in mydoc:
                    array= key["objects"]
                    print(len(array))
                    if len(array) > len(names_1):
                        a.clear() 
                        print("ikinci > birinci")
                        for y in array:
                            names_2.append(y["name"])
                            b.append(y["count"])    
                        print(b)
                        for y in array:
                            no_item = 0
                            for z in names_1:
                                if z == y["name"]:
                                    a.append(y["count"])
                                    no_item = 1
                            if no_item == 0:        
                                a.append(0)
                        print(a)

                        names_2.clear()
                
                    else:    
                        print("ikinci < birinci")
                        a=copy.copy(tmp)
                        for z in names_1:
                            no_item=0
                            for y in array:
                                if y["name"] == z:
                                    b.append(y["count"])
                                    no_item=1
                            if no_item==0:
                                b.append(0)
                        print(a)
                        print(b)
                    result=cosine_similarity([a],[b])
                    if result >= 0.5:
                        similar.append(name)  
                    print(result)
                    a.clear()
                    b.clear()
        print("ilk iterasyon sonu")
        names_1.clear()
        print(similar)
    
        bolean=mycollection2.find({"name": query}).count()  
        print(bolean)
        if bolean is 0:
    #        print("buradayım non")
            mycollection2.insert_one({"name":query, "similar_images":similar})
        else:
            mycollection2.update_one({"name": query},{ "$set" :{"similar_images":similar}})
        similar.clear()
    print("#######")

#similarityService()

