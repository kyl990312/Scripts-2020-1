
# -*- coding:utf-8 -*-
from xml.dom.minidom import parseString
import urllib.request
url ='http://www.career.go.kr/cnet/openapi/getOpenApi?apiKey=f69311384cfad095723cfa18c740c10b&svcType=api'
response_body =None

def setURL(str):
    str = '&svcCode=MAJOR&contentType=xml&gubun=univ_list'
    global url
    url += str

def RequestXML():
    global response_body, rescode
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        return response_body
    else:
        print("error code: "+rescode)
        return None

def PrintXML():
    print(response_body.decode('utf-8'))

setURL('')
RequestXML()
PrintXML()
