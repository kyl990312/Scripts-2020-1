import map
from loading import Data
from tkinter import *
from urllib.parse import quote
from urllib.request import Request
import requests
import ssl
import json
#import spam
from PIL import Image,ImageTk
import graph        # 그래프를 그리는데 필요
from tkinter import font
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus
import brouser
import mail

listbox = None
curMajor =''
checkVal0=None
checkVal1=None
checkVal2=None
checkVal3=None
checkVal4=None
checkVal5=None
checkVal6=None

uniNameL = None
uniLocationL = None
uniCampusL = None
uniUrlL = None

employRateG = None
satisG = None
aftergraduateG = None
salary = None
salaryL = None
salaryGL = None
jobL = None
jobDataL = None
qualificationL = None
qualificationDataL = None

majorNameL = None
majorClassLm = None
departmentL = None
departmentDataL = None
main_subjectL = None
main_subjectDataL = None
filedL = None
filedDataL = None
genderG = None


def checkLogger():
    map.logger.setLevel(map._logging.INFO)
    stream_handler = map._logging.StreamHandler()
    formatter = map._logging.Formatter("[%(filename)s] %(message)s")
    stream_handler.setFormatter(formatter)
    map.logger.addHandler(stream_handler)
    map.logger.info("CEF Python {ver}".format(ver=map.cef.__version__))
    map.logger.info("Python {ver} {arch}".format(
        ver=map.platform.python_version(), arch=map.platform.architecture()[0]))
    map.logger.info("Tk {ver}".format(ver=map.tk.Tcl().eval('info patchlevel')))
    assert map.cef.__version__ >= "55.3", "CEF Python v55.3+ required to run this"
    sys.excepthook = map.cef.ExceptHook  # To shutdown all CEF processes on error
    # Tk must be initialized before CEF otherwise fatal error (Issue #306)


def setMajorFrame():
    # 학과 이름 입력
    majorL = Label(MajorFrame, text="학과 이름", bg='light goldenrod1')
    majorL.grid(row=0, column=0)
    major = Entry(MajorFrame, width=15)
    major.grid(row=1, column=0)
    # 학과 이름 입력 후 오케이 버튼
    Button(MajorFrame, text="OK", bg='light goldenrod1', width=5, command=lambda X=major: OKProcess(X)).grid(row=1, column=1)
    MajorFrame.place(x=25, y=70)


def setUniFrame():
    global listbox
    UniFrame.place(x=25, y=260)
    # 학교 이름
    Label(UniFrame, text="해당 과가 있는 학교", width=15, height=1, bg='light goldenrod1').grid(row=0, column=0)
    listbox = Listbox(UniFrame, width=21, height=15)
    listbox.grid(row=1, column=0)
    Button(UniFrame, text="검색", bg='light goldenrod1', command=SearchProcess).grid(row = 2, column = 0)


def setFrame():
    frame0.place(x=220,y= 60)
    # 프레임 1 : 학교 정보 // 프레임 2 : 학과 정보 // 프레임 3 : 취업 정보
    nameLst = ["학교 정보" , "학과 정보", "취업 정보", "사람인"]
    for i in range(4):
        Button(frame0, text=nameLst[i],bg='sandy brown', command=lambda X=i: pressed(X)).pack(side=LEFT)
        frames.append(Frame(window, relief = "solid", highlightbackground = "gray20", highlightcolor = "gray20", highlightthickness=10))
        frames[i].place(x=220,y=85)
        Scrollbar(frames[i]).pack(side="right", fill="y")
        label = Label(frames[i],bg='orange', width=77, height=30)
        label.pack()
    Button(window, text = '메일', command = sendMail, width=5, height=1, bg='sandy brown').place(x = 700, y= 20)


def setLegion():
    # 지역 분류 : 0.서울 특별시, 1. 수도권: 경기도 + 인천, 2. 충청도, 3. 강원도, 4. 전라도 + 광주 + 대전, 5. 경상도 + 대구 + 부산, 6.제주특별자치구
    LegionFrame.place(x=25, y=130)

    Label(LegionFrame, text="지역", width=15, bg='light goldenrod1').place(x = 12.5 , y=0)
    global checkVal0, checkVal1, checkVal2, checkVal3, checkVal4, checkVal5, checkVal6
    checkVal0 = IntVar()
    checkVal1 = IntVar()
    checkVal2 = IntVar()
    checkVal3 = IntVar()
    checkVal4 = IntVar()
    checkVal5 = IntVar()
    checkVal6 = IntVar()
    checkList = [Checkbutton(LegionFrame, variable=checkVal0, text="서울", bg='light goldenrod1'),
                 Checkbutton(LegionFrame, variable=checkVal1,  text="수도권", bg='light goldenrod1'),
                 Checkbutton(LegionFrame, variable=checkVal2, text="충청도", bg='light goldenrod1'),
                 Checkbutton(LegionFrame, variable=checkVal3, text="강원도", bg='light goldenrod1'),
                 Checkbutton(LegionFrame, variable=checkVal4, text="전라도,광주,대전", bg='light goldenrod1'),
                 Checkbutton(LegionFrame, variable=checkVal5,  text="경상도,대구,부산", bg='light goldenrod1'),
                 Checkbutton(LegionFrame, variable=checkVal6,  text="제주", bg='light goldenrod1')]
    checkList[0].place(x = 0 , y=20)
    checkList[1].place(x = 70 , y=20)
    checkList[2].place(x = 0 , y=40)
    checkList[3].place(x = 70 , y=40)
    checkList[4].place(x = 0 , y=60)
    checkList[5].place(x = 0 , y=80)
    checkList[6].place(x = 0 , y=100)


def getMap(name):
    # 검색할 주소 선
    # 선택한 대학교를 넣으면 됨
    # Production(실제 서비스) 환경
    URL = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyC68wSjaTQgd3T9GfGDeNc3PD7W-OLZ4YE' \
          '&sensor=false&language=ko&address={}'.format(name)

    # URL로 보낸 Requst의 Response를 response 변수에 할당
    response = requests.get(URL)

    # JSON 파싱
    data = response.json()

    # lat, lon 추출
    lat = data['results'][0]['geometry']['location']['lat']
    lng = data['results'][0]['geometry']['location']['lng']

    m = map.folium.Map(location=[lat, lng],
                       tiles="OpenStreetMap",
                       zoom_start=15)

    map.folium.CircleMarker(location=[lat, lng],
                            radius=10,  # 원의 크기
                            color="#000",  # 테두리색
                            fill_color="#fff",  # 채우기색
                            popup="Center of seoul").add_to(m)

    map.folium.Marker([lat, lng], popup=name).add_to(m)

    m.save('map.html')

def findImage(name):
    baseUrl = 'https://search.naver.com/search.naver?where=image&section=dic&query='
    plusUrl = '&ie=utf8&sm=tab_kld'

    url = baseUrl + quote_plus(name) + plusUrl# 한글 검색 자동 변환
    html = urlopen(url)
    soup = bs(html, "html.parser")
    img = soup.find_all(class_='_img')

    n = 1
    c = 0

    for i in img:
        imgUrl = i['data-source']
        with urlopen(imgUrl) as f:
            with open('uni' + '.png', 'wb') as h:  # w - write b - binary
                img = f.read()
                h.write(img)
        c += 1
        if(c == n):
            break

    image = ImageTk.PhotoImage(Image.open("uni.png"))
    a=Label(frames[0], image=image, height=100, width=200)
    a.image = image
    a.place(x=330, y= 120)
    print('다운로드 완료')


def OKProcess(major):
    global curMajor
    if major.get() != curMajor:
        print("make {0} data...".format(major.get()))
        datas.MakeUniversityData(major.get())   # 학과에 해당하는 대학정보를 만든다
        if len(datas.UniDict) is 0:
            return
        curMajor = major

        # 학과와 직업 정보를 생성한다.
        datas.MakeJobData()
        datas.MakeMajorData()

        datas.majorData.show()
        datas.jobData.show()
        
        # 학과 정보를 프레임에 띄워준다
        SetMajorDataToFrame()

        # 취업 정보를 프레임에 띄워준다
        SetJobDataToFrame()

    InputUniVersityToList(datas.UniDict)


def InputUniVersityToList(unilist):
    listbox.delete(0,listbox.size())
    key =''
    if checkVal0.get() == 1:
        key += "서울특별시/세종특별자치시/"
    if checkVal1.get() == 1:
        key += "경기도/인천광역시/"
    if checkVal2.get() == 1:
        key += "충청북도/충청남도/"
    if checkVal3.get() == 1:
        key += "강원도/"
    if checkVal4.get() == 1:
        key += "전라북도/전라남도/대전광역시/광주광역시/"
    if checkVal5.get() == 1:
        key += "경상북도/경상남도/대구광역시/부산광역시/"
    if checkVal6.get() == 1:
        key += "제주특별시/"
    lst = ''
    if key != '':
        for uni in unilist:
            lst += (uni + "/" + datas.UniDict[uni].area + "/")
        #lst = spam.select(key, lst)
    else:
        for uni in unilist:
            lst += (uni + "/" )
        #lst = spam.sort(lst)
    nameLst = lst.split("/")

    idx = 0
    for n in nameLst:
        if n != '':
            listbox.insert(idx,n)
            idx += 1


def SearchProcess():
    # list에서 대학을 선택한후 "검색" 버튼을 눌렀을때 실행된다
    # 선택한 항목을 튜플 (index, value) 값으로 받아온다.
    selection = listbox.curselection()
    # 대학을 선택하지 않고 "검색"을 누른경우는 return을 해 아무것도 실행하지 않도록 한다
    if len(selection) is 0:
        return

    # 선택한 list 항목의 대학이름이다
    name = listbox.get(selection[0])
    global uniNameL, uniLocationL, uniCampusL, uniUrlL
    # 대학의 이름을 통해 datas.uniDict에 접근하여 대학 정보를 프레임에 띄워주면 된다.
    getMap(name)  # 지도 추출
    uniNameL.configure(text = '학교 이름 : ' + name)
    uniLocationL.configure(text = '위치 지역 : ' + datas.UniDict[name].area)
    uniCampusL.configure(text = '캠퍼스 이름 : ' +datas.UniDict[name].campusName)
    uniUrlL.configure(text='홈페이지 : ' +datas.UniDict[name].url)

    findImage(name)


def SetMajorDataToFrame():
    global majorNameL, majorClassLm, departmentL, departmentDataL, main_subjectL, main_subjectDataL, filedL, filedDataL, genderG
    # text 정보를 넣어준다
    majorNameL.configure(text="학과 이름 : " + datas.major)
    majorClassLm.configure(text='학과 계열 : ' + datas.majorData.subject)
    departmentDataL.configure(text=datas.majorData.department)
    main_subjectDataL.configure(text=datas.majorData.main_subjects)
    filedDataL.configure(text=datas.majorData.graduates)

    # 입학상황에대한 그래프를 만든다
    genderG.SetData(datas.majorData.gender)
    genderG.DrawCircleGraph( ['sky blue', 'salmon'], 'gender')

def SetJobDataToFrame():
    global employRateG, satisG, aftergraduateG, salary, salaryL, jobL, jobDataL, qualificationL, qualificationDataL
    # 취업률 그래프를 만들어 그린다
    employRateG.SetData(datas.jobData.employmentRate)
    employRateG.DrawVerticalGraph(['MediumPurple1','LightPink2','SkyBlue2'],'employ')

    #만족도
    satisG.SetData(datas.jobData.satisfaction)
    satisG.DrawHorisontalGraph(['DarkOrchid4','DarkOrchid1','SlateBlue1','RoyalBlue1','SteelBlue1'],'satisfaction')

    # 상황
    aftergraduateG.SetData(datas.jobData.afterGraduation)
    aftergraduateG.DrawHorisontalGraph(['gray', 'red', 'SlateBlue1'],'afterGraduate')

    # 임금
    gData = {}
    for i in datas.jobData.salary:
        gData[i] = datas.jobData.salary[i]
    lst = [i for i in datas.jobData.salary]
    del(gData[lst[0]])
    salary.SetData(gData)
    salary.DrawCircleGraph(['sky blue', 'salmon','gray','pink','red'], 'salary')
    salaryL.configure(text = "평균 : " + datas.jobData.salary[lst[0]])

    # 기타 정보
    jobDataL.configure( text= datas.jobData.job)
    qualificationDataL.configure(text = datas.jobData.qualification)

def MakeFrameDatas():
    print("make frames...")
    global uniNameL, uniLocationL, uniCampusL, uniUrlL
    # 대학의 이름을 통해 datas.uniDict에 접근하여 대학 정보를 프레임에 띄워주면 된다.
    fontStyle = font.Font(frames[0], size=9, family='맑은 고딕')
    uniNameL = Label(frames[0], text='학교 이름 : ', bg='orange', font=fontStyle)
    uniNameL.place(x=350, y=30)
    uniLocationL = Label(frames[0], text='위치 지역 : ', bg='orange', font=fontStyle)
    uniLocationL.place(x=350, y=50)
    uniCampusL = Label(frames[0], text='캠퍼스 이름 : ', bg='orange', font=fontStyle)
    uniCampusL.place(x=350, y=70)
    uniUrlL = Label(frames[0], text='홈페이지 : ', bg='orange', font=fontStyle)
    uniUrlL.place(x=350, y=90)

    # 취업정보 frame
    fontStyle = font.Font(frames[2], size=9, family='맑은 고딕')
    global employRateG, satisG, aftergraduateG, salary, salaryL, salaryGL, jobL, jobDataL, qualificationL, qualificationDataL
    # 취업률 그래프를 만들어 그린다
    employRateG = graph.Graph(frames[2], 'orange', 150, 150, 20, 10, '')
    Label(frames[2], text="취업률 그래프", bg='orange', font=fontStyle).place(x=80, y=180)
    # 만족도
    satisG = graph.Graph(frames[2], 'orange', 200, 100, 20, 210, '')
    Label(frames[2], text="첫 직장 만족도", bg='orange', font=fontStyle).place(x=80, y=310)
    # 상황
    aftergraduateG = graph.Graph(frames[2], 'orange', 200, 100, 20, 330, '')
    Label(frames[2], text="졸업 후 상황", bg='orange', font=fontStyle).place(x=80, y=430)
    # 임금
    salary = graph.Graph(frames[2], 'orange', 200, 200, 300, 20, '')
    salaryL = Label(frames[2], text="평균 : ", bg='orange', font=fontStyle)
    salaryL.place(x=340, y=220)
    Label(frames[2], text="임금 그래프", bg='orange', font=fontStyle).place(x=380, y=240)
    # 기타 정보
    jobL = Label(frames[2], text='관련 직업', bg='orange', font=fontStyle)
    jobL.place(x=230, y=260)
    jobDataL = Label(frames[2], text='', bg='orange', font=fontStyle, wraplength=300)
    jobDataL.place(x=240, y=280)
    qualificationL = Label(frames[2], text='관련 자격', bg='orange', font=fontStyle)
    qualificationL.place(x=230, y=360)
    qualificationDataL = Label(frames[2], text='', bg='orange', font=fontStyle, wraplength=300)
    qualificationDataL.place(x=240, y=380)

    # 학과정보 Frame
    global majorNameL, majorClassLm, departmentL,departmentDataL, main_subjectL,main_subjectDataL, filedL, filedDataL, genderG
    fontStyle = font.Font(frames[1], size=9, family='맑은 고딕')  # 폰트를 설정해 준다
    # text 정보를 넣어준다
    majorNameL = Label(frames[1], text="학과 이름 : ", bg='orange', font=fontStyle)
    majorNameL.place(x=20, y=30)
    majorClassLm=Label(frames[1], text='학과 계열 : ', bg='orange', font=fontStyle)
    majorClassLm.place(x=20, y=50)
    Label(frames[1], text="세부 관련 학과", bg='orange', font=fontStyle).place(x=20, y=70)
    departmentDataL = Label(frames[1], text='', bg='orange', font=fontStyle, wraplength=250)
    departmentDataL.place(x=30, y=90)
    Label(frames[1], text="주요 과목", font=fontStyle, bg='orange').place(x=20, y=300)
    main_subjectDataL= Label(frames[1], text='', bg='orange', font=fontStyle, wraplength=500)
    main_subjectDataL.place(x=30, y=320)
    Label(frames[1], text="졸업 후 진출 분야", font=fontStyle, bg='orange').place(x=20, y=370)
    filedDataL = Label(frames[1], text='', bg='orange', font=fontStyle, wraplength=500)
    filedDataL.place(x=30, y=390)
    # 입학상황에대한 그래프를 만든다
    genderG = graph.Graph(frames[1], 'orange', 200, 200, 320, 70, '')

def pressed(X):
    frames[X].tkraise()
    if X == 0:
        toplevel.deiconify()
        toplevel.attributes('-topmost', 'true')
    else:
        toplevel.withdraw()

    if X == 3:
        toplevel2.deiconify()
        toplevel2.attributes('-topmost', 'true')
    else:
        toplevel2.withdraw()


def windowPlace():
    width_window = 800
    height_window = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coord = (screen_width / 2) - (width_window / 2)
    y_coord = (screen_height / 2) - (height_window / 2)

    window.geometry("%dx%d+%d+%d" % (width_window, height_window, x_coord, y_coord))

    width_window = 300
    height_window = 300
    x_coord = (screen_width / 2) - ((window.winfo_x() + 300) / 2)
    y_coord = (screen_height / 2) - ((window.winfo_y() + 300) / 2)

    toplevel.geometry("%dx%d+%d+%d"%(width_window, height_window, x_coord, y_coord))

    toplevel.overrideredirect(1)
    window.overrideredirect(1)

    width_window = 500
    height_window = 450
    x_coord = (screen_width / 2) - ((window.winfo_x() + 300) / 2)
    y_coord = (screen_height / 2) - ((window.winfo_y() + 410) / 2)

    toplevel2.geometry("%dx%d+%d+%d" % (width_window, height_window, x_coord, y_coord))

    toplevel2.overrideredirect(1)


def esc(event):
    window.destroy()


def sendMail():
    if datas.majorData:
        m = mail.Mail()
        m.SendMail(datas)


if __name__ == '__main__':
    checkLogger()               #버전과 컴퓨터 환경 확인
    window = Tk()  # 윈도우 생성
    window.configure(bg='LightGoldenrod1')

    backImage = PhotoImage(file='back.png')
    back = Label(window, image=backImage, bg='LightGoldenrod1')
    back.place(x=0, y=0)

    toplevel = Toplevel(window, width=window.winfo_width(), height=window.winfo_height())#외부 윈도우 생성 // 지도 그리는 윈도우
    toplevel2 = Toplevel(window, width=window.winfo_width(), height=window.winfo_height())  # 외부 윈도우 생성 // 지도 그리는 윈도우
    windowPlace()               #윈도우 배치
    window.bind("<Escape>", esc)
    datas = Data()  # 검색하는 학과의 정보를 담는다.

    blackImage = PhotoImage(file='black.png')
    black = Label(window, image=blackImage, bg='gold', width = 180, height = 500)
    black.place(x=10, y = 60)

    MajorFrame = Frame(window, bg='light goldenrod1')
    UniFrame = Frame(window, bg='light goldenrod1')
    LegionFrame = Frame(window, width = 150, height= 120, bg='light goldenrod1')

    frame0 = Frame(window)
    frames = []

    setMajorFrame()
    setLegion()
    setUniFrame()
    setFrame()
    MakeFrameDatas()

    map.MainFrame(toplevel)
    map.cef.Initialize()
    brouser.MainFrame(toplevel2)
    brouser.cef.Initialize()
    window.mainloop()
    map.cef.Shutdown()