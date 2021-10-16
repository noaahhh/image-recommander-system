from imageai.Detection import ObjectDetection
import os
from manageDb import save2Db
from similarity import similarityService
#ciktinin üretilmesi zaman aliyor olabilir.

def saveImageInfo2Db(filename):
    
    #filename = request.args.get("filename")
    execution_path = "/home/username/services"
    imagefile_path ="/home/username/files"
    outputfile_path="/home/username/out"
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(imagefile_path , filename), output_image_path=os.path.join(outputfile_path , "output.jpg"))

    output = "SONUCLAR: | "
    detectedObject=[]
    for eachObject in detections:
        output = output + "  |  " + eachObject["name"] + " : " + str(eachObject["percentage_probability"] )
        detectedObject.append(eachObject["name"])
    
    print(detectedObject)
    resultObject=save2Db( filename, detectedObject)
    if resultObject.acknowledged is True:
        similarityService()
    
    return output

