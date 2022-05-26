#!/usr/bin/env python3
import cv2
import http.client, urllib.request, urllib.parse, urllib.error, base64
import requests
import io
from time import gmtime, strftime

#from mistyPy.Robot import Robot
#from mistyPy.Events import Events





headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'b0365b4ab3c34adeb907cf3fae911f02',
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,emotion',
    'recognitionModel': 'recognition_04',
    'returnRecognitionModel': 'false',
    'detectionModel': 'detection_01',
    'faceIdTimeToLive': '86400',
})

def get_emotions_of(image):

    img_name = "img_{}.png".format(strftime("%Y%m%d%H%M%S"))
    cv2.imwrite(img_name, image)
    try:
        response = requests.post('https://misty-human-interaction.cognitiveservices.azure.com/face/v1.0/detect?detectionModel=detection_01&returnFaceAttributes=age,gender,emotion&faceIdTimeToLive=86400&returnRecognitionModel=false&recognitionModel=recognition_04', headers=headers, data=open(img_name, 'rb').read())

        return response.json()[0]['faceAttributes']['emotion']
    except Exception as e:
        print(e)

    return {}

def numpy_to_binary(arr):
    is_success, buffer = cv2.imencode(".jpg", arr)
    io_buf = io.BytesIO(buffer)
    print(type(io_buf))
    return io_buf.read()
