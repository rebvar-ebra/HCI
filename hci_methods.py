from re import L


import request
import numpy as np
from gtts import gTTS
import mistyPy
from mistyPy.Robot import Robot
from mistyPy.Events import Events

from base64 import b64encode, b64decode
import time

import cv2

#misty = Robot("10.0.1.206")
#misty = Robot("10.2.8.5")

def default_image_classification_algorithm(image,misty):

    # Write your own method here...
    # At the moment we are just displaying the image
    # HAMMER Classification Algorithm
    emotions = request.get_emotions_of(image)
    print(emotions)
    emotion = max(emotions, key=emotions.get)

    print(set_emotion(emotion, misty))
    

    
    


def set_emotion(emotion, misty):

    if(emotion == 'anger'):
        misty.DisplayImage('e_Anger.jpg')
        misty.changeLED(252, 73, 3) # Red
        text="you are angry"
        lang="en"
        output=gTTS(text=text,lang=lang,slow=False)
        output.save("tts_output.wav")
        
        with open("tts_output.wav", "rb") as wav_file:
            base64_str = str(b64encode(wav_file.read()), 'ascii', 'ignore')
            print(misty.SaveAudio(file_name, base64_str, True, True))
        
        return "anger"

    if(emotion == 'contempt'):
        misty.DisplayImage('e_Contempt.jpg')
        misty.changeLED(3, 53, 252) # 
        text="you face like contempt"
        lang="en"
        output=gTTS(text=text,lang=lang,slow=False)
        output.save("tts_output.wav")
        with open("tts_output.wav", "rb") as wav_file:
            base64_str = str(b64encode(wav_file.read()), 'ascii', 'ignore')
            print(misty.SaveAudio("tts_output.wav", base64_str, True, True))
        return "contempt"
    if(emotion == 'disgust'):
        misty.DisplayImage('e_Disgust.jpg')
        misty.changeLED(199, 207, 60) # 
        text="you feel like disgust"
        lang="en"
        output=gTTS(text=text,lang=lang,slow=False)
        output.save("tts_output.wav")
        with open("tts_output.wav", "rb") as wav_file:
            base64_str = str(b64encode(wav_file.read()), 'ascii', 'ignore')
            print(misty.SaveAudio("tts_output.wav", base64_str, True, True))
        return "disgust"
        
    if(emotion == 'fear'):
        misty.DisplayImage('e_Fear.jpg')
        misty.changeLED(5, 237, 222) # Purple
        text="are you scare?"
        lang="en"
        output=gTTS(text=text,lang=lang,slow=False)
        output.save("tts_output.wav")
        with open("tts_output.wav", "rb") as wav_file:
            base64_str = str(b64encode(wav_file.read()), 'ascii', 'ignore')
            print(misty.SaveAudio("tts_output.wav", base64_str, True, True))
        return "fear"
        
    if(emotion == 'happiness'):
        misty.DisplayImage('e_Love.jpg')
        misty.changeLED(237, 5, 24)# 
        text="you're look like happy"
        lang="en"
        output=gTTS(text=text,lang=lang,slow=False)
        output.save("tts_output.wav")
        with open("tts_output.wav", "rb") as wav_file:
            base64_str = str(b64encode(wav_file.read()), 'ascii', 'ignore')
            print(misty.SaveAudio("tts_output.wav", base64_str, True, True))
        return "happiness"
        
    if(emotion == 'neutral'):
        misty.DisplayImage('e_EcstacyStarryEyed.jpg')
        misty.changeLED(242, 175, 68) # 
        text="you are neutral"
        lang="en"
        output=gTTS(text=text,lang=lang,slow=False)
        output.save("tts_output.wav")
        with open("tts_output.wav", "rb") as wav_file:
            base64_str = str(b64encode(wav_file.read()), 'ascii', 'ignore')
            print(misty.SaveAudio("tts_output.wav", base64_str, True, True))
        return "neutral"
          
    if(emotion == 'sadness'):
        misty.DisplayImage('e_Sadness.jpg')
        misty.changeLED(0,200,255) # 
        text="why are you sad"
        lang="en"
        output=gTTS(text=text,lang=lang,slow=False)
        output.save("tts_output.wav")
        with open("tts_output.wav", "rb") as wav_file:
            base64_str = str(b64encode(wav_file.read()), 'ascii', 'ignore')
            print(misty.SaveAudio("tts_output.wav", base64_str, True, True))
        return "sadness"
        
    if(emotion == 'surprise'):
        misty.DisplayImage('e_Amazement.jpg')
        misty.changeLED(115, 252, 3) # Green
        text="what happend"
        lang="en"
        output=gTTS(text=text,lang=lang,slow=False)
        output.save("tts_output.wav")
        with open("tts_output.wav", "rb") as wav_file:
            base64_str = str(b64encode(wav_file.read()), 'ascii', 'ignore')
            print(misty.SaveAudio("tts_output.wav", base64_str, True, True))
        return "surprise"

#default_image_classification_algorithm({})
