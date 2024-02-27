import subprocess
import os
import sys
import json
import requests
from PIL import Image

def GetFile():
    cmd = "ffmpeg -y -i rtsp://admin:password@192.168.0.101:554/h264Preview_01_main -vframes 1 BrightnessTest.jpg"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    p.communicate()
    print("File is here")

def CheckBrightness():
    filename = "BrightnessTest.jpg"
    if(os.path.isfile(filename)):
        with Image.open(filename) as img:
            img.load()
            gray_img = img.convert("L")
            #gray_img.show()
            pixels = list(gray_img.getdata())
            lumaMax = 255 * gray_img.width * gray_img.height
            lumaPix=sum(pixels)
            lumaR = (lumaPix / lumaMax)*100
            print(len(pixels))
            print(lumaPix)
            print(lumaR)
            return lumaR
    else:
            print("File does nor exist")
            return -1

def SetBlackandWhite():
    url = "https://192.168.0.101/api.cgi?cmd=Login"
    myobj = [{"cmd": "Login", "param": {"User": {"Version": "0", "userName": "admin", "password": "password"}}}]
    response = requests.post(url, json=myobj, verify=False)
    print(response.text)
    t = json.loads(response.text)
    token = t[0]["value"]["Token"]["name"]

    url = "https://192.168.0.101/api.cgi?cmd=SetIsp&token=" + token
    CmdJson = [{"cmd": "SetIsp", "action": 0, "param": {"Isp": {"dayNight": "Black&White"}}}]
    response = requests.post(url, json=CmdJson, verify=False)
    print(response.text)

def SetColor():
    url = "https://192.168.0.101/api.cgi?cmd=Login"
    myobj = [
        {"cmd": "Login", "param": {"User": {"Version": "0", "userName": "admin", "password": "password"}}}]
    response = requests.post(url, json=myobj, verify=False)
    print(response.text)
    t = json.loads(response.text)
    token = t[0]["value"]["Token"]["name"]

    url = "https://192.168.0.101/api.cgi?cmd=SetIsp&token=" + token
    CmdJson = [{"cmd": "SetIsp", "action": 0, "param": {"Isp": {"dayNight": "Color"}}}]
    response = requests.post(url, json=CmdJson, verify=False)
    print(response.text)

GetFile()

CheckBrightness()
#BrightnessTreshold in %
lumaTreshold = 10 
print (sys.argv[1])
if (len(sys.argv)>0):
    if(sys.argv[1]=="CheckBrightness"):
        cbv = CheckBrightness()
        if(cbv>0) and (cbv<=lumaTreshold):
            SetBlackandWhite()
            print("Set Black and White mode.")

    if(sys.argv[1]=="SetColor"):
        SetColor()
        print("Set Color Mode.")
else:
    print("No arguments")
