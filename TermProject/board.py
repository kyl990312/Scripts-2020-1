import map
from loading import Data
from tkinter import *
from urllib.parse import quote
from urllib.request import Request, urlopen
import requests
import ssl
import json
#import spam
from PIL import Image,ImageTk

listbox = None
curMajor =''
checkVal0=None
checkVal1=None
checkVal2=None
checkVal3=None
checkVal4=None
checkVal5=None
checkVal6=None


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
    for i in range(3):
        Button(frame0, text="Frame" + str(i),bg='sandy brown', command=lambda X=i: pressed(X)).pack(side=LEFT)
        frames.append(Frame(window, relief = "solid", highlightbackground = "gray20", highlightcolor = "gray20", highlightthickness=10))
        frames[i].place(x=220,y=85)
        label = Label(frames[i], text="Frame" + str(i),bg='orange', width=77, height=30)
        label.pack()


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

    m.save('D:\document\map.html')


def OKProcess(major):
    global curMajor
    if major != curMajor:
        datas.MakeUniversityData(major.get())   # 학과에 해당하는 대학정보를 만든다
        if len(datas.UniDict) is 0:
            return
        curMajor = major

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
    for uni in unilist:
        lst += (uni + "/" + datas.UniDict[uni].area + "/")
    #if key != '':
        #lst = spam.select(key, lst)
    #else:
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

    # 대학을 선택하고 버튼을 누른경우 학과와 직업 정보를 생성한다.
    datas.MakeJobData()
    datas.MakeMajorData()

    # 선택한 list 항목의 대학이름이다
    name = listbox.get(selection[0])

    # 대학의 이름을 통해 datas.uniDict에 접근하여 대학 정보를 프레임에 띄워주면 된다.
    datas.UniDict[name].show()
    getMap(name)  # 지도 추출
    Label(frames[0], text = '학교 이름 : ' + name).place(x=350, y=30)
    Label(frames[0], text = '위치 지역 : ' + datas.UniDict[name].area).place(x=350, y=50)
    Label(frames[0], text = '캠퍼스 이름 : ' +datas.UniDict[name].campusName).place(x=350, y=70)
    Label(frames[0], text='홈페이지 : ' +datas.UniDict[name].url).place(x=350, y=90)


def pressed(X):
    frames[X].tkraise()
    if X == 0:
        toplevel.deiconify()
        toplevel.attributes('-topmost', 'true')
    else:
        toplevel.withdraw()


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
    x_coord = (screen_width / 2) - (width_window / 2)
    y_coord = (screen_height / 2) - (height_window / 2)

    toplevel.geometry("%dx%d+%d+%d"%(width_window, height_window, x_coord, y_coord))

    window.resizable(0, 0)
    toplevel.resizable(0, 0)

    toplevel.overrideredirect(1)


if __name__ == '__main__':
    checkLogger()               #버전과 컴퓨터 환경 확인
    window = Tk()  # 윈도우 생성
    window.configure(bg='LightGoldenrod1')

    backImage = PhotoImage(file='back.png')
    back = Label(window, image=backImage, bg='LightGoldenrod1')
    back.place(x=0, y=0)

    toplevel = Toplevel(window, width=window.winfo_width(), height=window.winfo_height())#외부 윈도우 생성 // 지도 그리는 윈도우
    windowPlace()               #윈도우 배치

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

    map.MainFrame(toplevel)
    map.cef.Initialize()
    window.mainloop()
    map.cef.Shutdown()