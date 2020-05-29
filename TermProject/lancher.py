from parsing import*
import urllib.parse
from Datas import*
import urllib.request
from xml.etree import ElementTree

def MakeUniDataByMajor(majorSeq):
    str ="&svcCode=MAJOR_VIEW&contentType=xml&gubun=univ_list&majorSeq="+majorSeq
    contentTree= MakeTree(str)
    contentElements = contentTree.iter('content')
    univercityList = []
    for c in contentElements:
        if c.find('area'):
            uni = University()
            area = c.find('area')
            schoolName = c.find('schoolName')
            url = c.find('schoolURL')
            uni.area = area.text
            uni.schoolName = schoolName.text
            uni.url = url.text
            univercityList.append(uni)






seqAndClass = ExtractmClassAndMajorSeq()
for i in seqAndClass:
    print(i)

while(True):
    key = input("학과를 정확하게 입력하세요: ")
    #찾고자 하는 학과의 majorSeq를 얻는다
    majorSeq = seqAndClass[key]
    MakeUniDataByMajor(majorSeq)




