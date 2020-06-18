
# -*- coding:utf-8 -*-
import urllib.request
from xml.etree import ElementTree
# 빨간줄 뜨면 file -> settings -> pakage + -> request install
import requests

def MakeURL(str):
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

def MakeTree(str):          # 요청변수를 받아 xml파일을 tree로 반환해주는 함수이다.
    # list xml 파싱
    url = MakeURL(str)
    listXmlFile = RequestXML(url)
    tree = ElementTree.fromstring(listXmlFile)
    return tree

from Datas import *
def ExtractmClassAndMajorSeq():
    contentTree = MakeTree('&svcCode=MAJOR&contentType=xml&gubun=univ_list&subject=100391')
    contentElements= contentTree.iter('content')
    dict = {}
    for content in contentElements:
        data = listURLData()
        mClass = content.find("mClass")
        majorSeq = content.find("majorSeq")
        subject = content.find('lClass')

        data.seq = majorSeq.text
        data.sbject = subject.text

        dict[mClass.text] = data

    contentTree = MakeTree('&svcCode=MAJOR&contentType=xml&gubun=univ_list&subject=100392')
    contentElements = contentTree.iter('content')

    for content in contentElements:
        data = listURLData()
        mClass = content.find("mClass")
        majorSeq = content.find("majorSeq")
        subject = content.find('lClass')

        data.seq = majorSeq.text
        data.sbject = subject.text

        dict[mClass.text] = data

    contentTree = MakeTree('&svcCode=MAJOR&contentType=xml&gubun=univ_list&subject=100393')
    contentElements = contentTree.iter('content')

    for content in contentElements:
        data = listURLData()
        mClass = content.find("mClass")
        majorSeq = content.find("majorSeq")
        subject = content.find('lClass')

        data.seq = majorSeq.text
        data.sbject = subject.text

        dict[mClass.text] = data

    contentTree = MakeTree('&svcCode=MAJOR&contentType=xml&gubun=univ_list&subject=100394')
    contentElements = contentTree.iter('content')

    for content in contentElements:
        data = listURLData()
        mClass = content.find("mClass")
        majorSeq = content.find("majorSeq")
        subject = content.find('lClass')

        data.seq = majorSeq.text
        data.sbject = subject.text

        dict[mClass.text] = data

    contentTree = MakeTree('&svcCode=MAJOR&contentType=xml&gubun=univ_list&subject=100395')
    contentElements = contentTree.iter('content')

    for content in contentElements:
        data = listURLData()
        mClass = content.find("mClass")
        majorSeq = content.find("majorSeq")
        subject = content.find('lClass')

        data.seq = majorSeq.text
        data.sbject = subject.text

        dict[mClass.text] = data

    contentTree = MakeTree('&svcCode=MAJOR&contentType=xml&gubun=univ_list&subject=100396')
    contentElements = contentTree.iter('content')

    for content in contentElements:
        data = listURLData()
        mClass = content.find("mClass")
        majorSeq = content.find("majorSeq")
        subject = content.find('lClass')

        data.seq = majorSeq.text
        data.sbject = subject.text

        dict[mClass.text] = data

    contentTree = MakeTree('&svcCode=MAJOR&contentType=xml&gubun=univ_list&subject=100397')
    contentElements = contentTree.iter('content')

    for content in contentElements:
        data = listURLData()
        mClass = content.find("mClass")
        majorSeq = content.find("majorSeq")
        subject = content.find('lClass')

        data.seq = majorSeq.text
        data.sbject = subject.text

        dict[mClass.text] = data
    return dict


def PasUniData():
    searching = '한국산업기술대학교'

    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(searching)
    headers = {
        "Authorization": "KakaoAK 729569259cfcf6680016148bd34f19fb"
    }
    places = requests.get(url, headers=headers).json()['documents']
