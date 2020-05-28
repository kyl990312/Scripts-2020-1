
# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
from xml.etree import ElementTree
def makeURL(str):
    url ='http://www.career.go.kr/cnet/openapi/getOpenApi?apiKey=f69311384cfad095723cfa18c740c10b&svcType=api' + str
    return url

def RequestXML(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        return response.read()
    else:
        print("error code: "+rescode)
        return None

def DataBuilder():
    # list xml 파싱
    url = makeURL('&svcCode=MAJOR&contentType=xml&gubun=univ_list')
    listXmlFile = RequestXML(url)
    #xml 문서에서 mClass와 majorSeq 추출
    tree = ElementTree.fromstring(listXmlFile)
    itemElements = tree.iter("content")
    dictList = []
    for item in itemElements:
        mClass = item.find("mClass")
        majorSeq = item.find("majorSeq")
        dictList.append({mClass.text : majorSeq.text})
    return dictList
