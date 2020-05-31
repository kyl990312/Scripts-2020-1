from parsing import*
from Datas import*

majorUniListDiction = {}        # 학과이름 : 학과가 있는 대학들의 정보
majorDataDiction = {}           # 학과이름 : 학과정보
jobDataDiction = {}             # 학과이름 : 취업정보
seqAndClass = {}                # 학과이름 : listURL에 있던 학과정보


def FindUniInList(uni,lst):
    for l in lst:
        if( uni.schoolName == l.schoolName) and (uni.campusName == l.campusName):
            return True
    return False

def UniqueList(lst):
    uniUniqueList = []
    for uni in lst:
        if not FindUniInList(uni,uniUniqueList):
            uniUniqueList.append(uni)
    return uniUniqueList

def MakeDataByMajorSeq(majorSeq):
    str ="&svcCode=MAJOR_VIEW&contentType=xml&gubun=univ_list&majorSeq="+majorSeq
    tree= MakeTree(str)

    majorData = Major()
    jobData = Job()
    univercityList = []
    for c in tree.iter('content'):
        if not(c.find('schoolName') is None):
            uni = University()
            schoolName = c.find('schoolName')
            campusName = c.find('campus_nm')
            area = c.find('area')
            url = c.find('schoolURL')
            uni.area = area.text
            uni.schoolName = schoolName.text
            uni.campusName = campusName.text
            uni.url = url.text
            univercityList.append(uni)
        elif not(c.find('SBJECT_NM') is None):
            subject = c.find('SBJECT_NM')
            majorData.main_subjects.append(subject.text)
        elif not(c.find('department') is None):
            department = c.find('department')
            majorData.department = department.text
        elif not (c.find('name') is None):
            if c.find('name').text == "졸업 후 첫 직업 분야":
                majorData.graduates.append(c.find('item').text)
            elif c.find('name').text == "취업률":
                jobData.employmentRate[c.find('item').text] = c.find('data').text
            elif c.find('name').text == "졸업 후 첫 직장 월평균 임금":
                jobData.salary[c.find('item').text] = c.find('data').text
            elif c.find('name').text == "첫 직장 만족도":
                jobData.satisfaction[c.find('item').text] = c.find('data').text
            elif c.find('name').text == "졸업 후 상황":
                jobData.afterGraduation[c.find('item').text] = c.find('data').text
        if not (c.find('job') is None):
            jobData.job = c.find('job').text
        if not (c.find('qualifications') is None):
            jobData.qualification = c.find('qualifications').text

    univercityList = UniqueList(univercityList)
    returnDataList = [univercityList,majorData,jobData]
    return returnDataList




def MakeDataByMajor(major):
    majorSeq = seqAndClass[major].seq
    lst = MakeDataByMajorSeq(majorSeq)
    if(lst.count == 0):
        print("no Data")
    print("<University Datas>")
    for uni in lst[0]:
        uni.show()
    print("\n<Major Datas>")
    lst[1].major = major
    lst[1].show()
    print('\n<Job Data>')
    lst[2].show()
    majorUniListDiction[major] = lst[0]
    majorDataDiction[major] = lst[1]


def Loading():
    global seqAndClass
    seqAndClass = ExtractmClassAndMajorSeq()
    for i in seqAndClass:
        MakeDataByMajor(i)
    dic = {"uni":majorUniListDiction , "major":majorDataDiction ,"job":jobDataDiction,'selectData':seqAndClass}
    return dic






