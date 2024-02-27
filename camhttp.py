import json
import requests

url = "https://192.168.1.104/api.cgi?cmd=Login"
myobj = [{"cmd": "Login", "param": {"User": {"Version": "0", "userName": "admin", "password": "password"}}}]
response = requests.post(url, json=myobj, verify=False)
print(response.text)
t = json.loads(response.text)
token = t[0]["value"]["Token"]["name"]

#token = "dd5f1e16f0501b4"
url = "https://192.168.1.104/api.cgi?cmd=SetIsp&token=" + token
#CmdJson = [{"cmd": "SetIsp", "action": 0, "param": {"Isp": {"exposure": "Anti-Smearing","shutter" : {"max" : 125,"min" : 100}}}}]
CmdJson = [{"cmd": "SetIsp", "action": 0, "param": {"Isp": {"exposure": "Auto","shutter" : {"max" : 125,"min" : 100}}}}]
response = requests.post(url, json=CmdJson, verify=False)
print(response.text)

url = "https://192.168.1.104/api.cgi?cmd=GetIsp&token=" + token

response = requests.get(url, verify=False)
print(response.text)
