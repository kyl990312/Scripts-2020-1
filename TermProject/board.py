from tkinter import *
import map
from loading import Data
<<<<<<< Updated upstream
=======
from tkinter import *
from urllib.parse import quote
from urllib.request import Request, urlopen
import requests
import ssl
import json

>>>>>>> Stashed changes

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
    Label(MajorFrame, text="학과 이름", width=15).grid(row=0, column=0)
    major = Entry(MajorFrame, width=15)
    major.grid(row=1, column=0)
    # 학과 이름 입력 후 오케이 버튼
    Button(MajorFrame, text="OK", width=5, command=lambda X=major: OKProcess(X)).grid(row=1, column=1)
    MajorFrame.grid(row=0, column=0)

def setUniFrame():
    UniFrame.grid(row=1, column=0)
    # 학교 이름
    Label(UniFrame, text="해당 과가 있는 학교", width=15, height=1).grid(row=8, column=0)
    listbox = Listbox(UniFrame, width=15, height=30)
    listbox.grid(row=9, column=0)

def setFrame():
    frame0.grid(row=0, column=1)
    # 프레임 1 : 학교 정보 // 프레임 2 : 학과 정보 // 프레임 3 : 취업 정보
    for i in range(3):
        Button(frame0, text="Frame" + str(i), command=lambda X=i: pressed(X)).pack(side=LEFT)
        frames.append(Frame(window))
        frames[i].grid(row=1, column=1)
        label = Label(frames[i], text="FRAME" + str(i), width=60, height=30)
        label.pack()

def setLegion():
    # 지역 분류 : 0.서울 특별시, 1. 수도권: 경기도 + 인천, 2. 충청도, 3. 강원도, 4. 전라도 + 광주 + 대전, 5. 경상도 + 대구 + 부산, 6.제주특별자치구
    Label(UniFrame, text="지역", width=15).grid(row=2, column=0)

    checkVal0 = IntVar()
    checkVal1 = IntVar()
    checkVal2 = IntVar()
    checkVal3 = IntVar()
    checkVal4 = IntVar()
    checkVal5 = IntVar()
    checkVal6 = IntVar()
    checkList = [Checkbutton(UniFrame, variable=checkVal0, width=5, height=1, text="서울"),
                 Checkbutton(UniFrame, variable=checkVal1, width=5, height=1, text="수도권"),
                 Checkbutton(UniFrame, variable=checkVal2, width=5, height=1, text="충청도"),
                 Checkbutton(UniFrame, variable=checkVal3, width=5, height=1, text="강원도"),
                 Checkbutton(UniFrame, variable=checkVal4, width=15, height=1, text="전라도,광주,대전"),
                 Checkbutton(UniFrame, variable=checkVal5, width=15, height=1, text="경상도,대구,부산"),
                 Checkbutton(UniFrame, variable=checkVal6, width=5, height=1, text="제주")]
    checkList[0].grid(row=3, column=0)
    checkList[1].grid(row=3, column=1)
    checkList[2].grid(row=4, column=0)
    checkList[3].grid(row=4, column=1)
    checkList[4].grid(row=5, column=0)
    checkList[5].grid(row=6, column=0)
    checkList[6].grid(row=7, column=0)

def getMap():
    # 검색할 주소
    location = '서현동'

    # Production(실제 서비스) 환경
    URL = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyC68wSjaTQgd3T9GfGDeNc3PD7W-OLZ4YE' \
          '&sensor=false&language=ko&address={}'.format(location)

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

    map.folium.Marker([lat, lng], popup=location).add_to(m)

    m.save('D:/document/3-1/map.html')

def setFrame():
    # 학과 이름
    Label(window, text="학과 이름", width=15).grid(row=0, column=0)
    # 학과 이름 입력
    Entry(window, width=15).grid(row=1, column=0)
    # 학과 이름 입력 후 오케이 버튼
    Button(window, text="OK", width=5).grid(row=1, column=1)
    # 학교 이름
    Label(window, text="해당 과가 있는 학교", width=15).grid(row=2, column=0)

    # 프레임 1 : 학교 정보 // 프레임 2 : 학과 정보 // 프레임 3 : 취업 정보
    for i in range(3):
        Button(frame0, text="Frame" + str(i), command=lambda X=i: pressed(X)).pack(side=LEFT)
        frames.append(Frame(window))
        frames[i].grid(row=3, column=2)
        label = Label(frames[i], text="FRAME" + str(i), width=10, height=10)
        label.pack()

def OKProcess(major):
    datas.MakeUniversityData(major.get())              # 학과에 해당하는 대학정보를 만든다
    InputUniVersityToList()

def InputUniVersityToList():
    applicableList = []
    idx = 0

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

    width_window = 1000
    height_window = 800

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
    checkLogger()
    getMap()

    window = Tk()
    toplevel = Toplevel(window, width=window.winfo_width(), height=window.winfo_height())

    windowPlace()

    frame0 = Frame(window)
    frame0.grid(row=1, column=2)
    frames = []

    getMap()                    #지도 추출

    checkLogger()               #버전과 컴퓨터 환경 확인

    window = Tk()               #윈도우 생성
    toplevel = Toplevel(window, width=window.winfo_width(), height=window.winfo_height())#외부 윈도우 생성 // 지도 그리는 윈도우
    windowPlace()               #윈도우 배치

    datas = Data()  # 검색하는 학과의 정보를 담는다.

    MajorFrame = Frame(window)
    UniFrame = Frame(window)
    frame0 = Frame(window)
    frames = []

    setMajorFrame()
    setUniFrame()
    setLegion()
    setFrame()

    map.MainFrame(toplevel)
    map.cef.Initialize()
    window.mainloop()
    map.cef.Shutdown()