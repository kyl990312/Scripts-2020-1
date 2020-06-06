from parsing import*
from Datas import*

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

class Data:
    def __init__(self):
        self.UniList= []  # 학과이름 : 학과가 있는 대학들의 정보
        self.majorData = None  # 학과이름 : 학과정보
        self.jobData = None  # 학과이름 : 취업정보
        self.seqAndClass = ExtractmClassAndMajorSeq()  # 학과이름 : listURL에 있던 학과정보
        self.tree = None

    def MakeMajorData(self,major):
        self.majorData = Major()
        for c in self.tree.iter('content'):
            if not (c.find('SBJECT_NM') is None):
                subject = c.find('SBJECT_NM')
                self.majorData.main_subjects.append(subject.text)
            elif not (c.find('department') is None):
                department = c.find('department')
                self.majorData.department = department.text
            elif not (c.find('name') is None):
                if c.find('name').text == "졸업 후 첫 직업 분야":
                    self.majorData.graduates.append(c.find('item').text)



    def MakeJobData(self,major):
        print("loading...")
        self.jobData = Job()
        for c in self.tree.iter('content'):
            if not (c.find('name') is None):
                if c.find('name').text == "취업률":
                    self.jobData.employmentRate[c.find('item').text] = c.find('data').text
                elif c.find('name').text == "졸업 후 첫 직장 월평균 임금":
                    self.jobData.salary[c.find('item').text] = c.find('data').text
                elif c.find('name').text == "첫 직장 만족도":
                    self.jobData.satisfaction[c.find('item').text] = c.find('data').text
                elif c.find('name').text == "졸업 후 상황":
                    self.jobData.afterGraduation[c.find('item').text] = c.find('data').text
            if not (c.find('job') is None):
                self.jobData.job = c.find('job').text
            if not (c.find('qualifications') is None):
                self.jobData.qualification = c.find('qualifications').text
            print('end')


    def MakeUniversityData(self,major):
        print("loading...")
        str = "&svcCode=MAJOR_VIEW&contentType=xml&gubun=univ_list&majorSeq=" + self.seqAndClass[major].seq
        self.tree = MakeTree(str)
        print("made tree")

        self.UniList.clear()
        for c in self.tree.iter('content'):
            if not (c.find('schoolName') is None):
                uni = University()
                schoolName = c.find('schoolName')
                campusName = c.find('campus_nm')
                area = c.find('area')
                url = c.find('schoolURL')
                uni.area = area.text
                uni.schoolName = schoolName.text
                uni.campusName = campusName.text
                uni.url = url.text
                self.UniList.append(uni)
        self.UniList = UniqueList(self.UniList)
        print("end")











