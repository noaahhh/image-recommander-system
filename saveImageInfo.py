from imageai.Detection import ObjectDetection
import os
from saveImagetoDb import generateJson
 

from flask import Flask
from flask import request
app = Flask(__name__)

#ciktinin üretilmesi zaman aliyor olabilir.

@app.route('/saveImageInfo', methods=['GET'])

def get():
    
    filename = request.args.get("filename")
    execution_path = os.getcwd()
    
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , filename), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

    output = "SONUCLAR: | "
    detectedObject=[]
    for eachObject in detections:
        output = output + "  |  " + eachObject["name"] + " : " + str(eachObject["percentage_probability"] )
        detectedObject.append(eachObject["name"])
    
    print(detectedObject)
    generateJson( filename, detectedObject)
    return(output)

app.run(host='46.101.154.46', port=5000)
