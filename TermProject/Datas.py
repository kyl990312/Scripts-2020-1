class University:
    def __init__(self):
        self.schoolName =''
        self.url =''
        self.univSe =''
        self.area =''
        self.campusName = ''

    def show(self):
        print("<"+self.schoolName+">")
        print("URL: " + self.url)
        print("univSe: "+ self.univSe)
        print("area: " + self.area)
        print("campusName: "+self.campusName)



class Major:
    def __init__(self):
        self.major =''      #학과이름
        self.subject =''       #학과 계열
        self.department =''     #세부 관련 학과
        self.main_subjects=[]   # 주요과목
        self.graduates =[]      # 졸업 후 취업 분야

    def show(self):
        print("major: {0}".format(self.major))
        print("subject: {0}".format(self.subject))
        print("department: {0}".format(self.department))
        print("main_subjects: {0}".format(self.main_subjects))
        print("graduates: {0}".format(self.graduates))

class Job:
    def __init__(self):
        self.employmentRate = {}        # 취업률
        self.salary = {}        # 임금
        self.satisfaction = {}    # 첫 직장 만족도
        self.afterGraduation = {}   # 졸업 후 상황
        self.job = ''          # 관련직업
        self.qualification = ''    # 관련자격

    def show(self):
        print("employmentRate: ")
        for i in self.employmentRate:
            print("{0} : {1}".format(i,self.employmentRate[i]))
        print("salary: ")
        for i in self.salary:
            print("{0} : {1}".format(i,self.salary[i]))
        print("satisfaction: ")
        for i in self.satisfaction:
            print("{0} : {1}".format(i, self.satisfaction[i]))
        print("afterGraduation: ")
        for i in self.afterGraduation:
            print("{0} : {1}".format(i, self.afterGraduation[i]))
        print("job: {0}".format(self.job))
        print("qualification: {0}".format(self.qualification))


class listURLData:
    def __init__(self):
        self.seq = ''
        self.sbject =''

class AfterGraduation:
    def __init__(self):
        self.item = ''
        self.data = ''
