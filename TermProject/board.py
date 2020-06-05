from tkinter import *
import map

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

def getMap():
    m = map.folium.Map(location=[37.564214, 127.001699],
                       tiles="OpenStreetMap",
                       zoom_start=15)

    map.folium.CircleMarker(location=[37.564214, 127.001699],
                            radius=100,  # 원의 크기
                            color="#000",  # 테두리색
                            fill_color="#fff",  # 채우기색
                            popup="Center of seoul").add_to(m)

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
    checkLogger()
    getMap()

    window = Tk()
    toplevel = Toplevel(window, width=window.winfo_width(), height=window.winfo_height())

    windowPlace()

    frame0 = Frame(window)
    frame0.grid(row=1, column=2)
    frames = []

    setFrame()

    map.MainFrame(toplevel)
    map.cef.Initialize()
    window.mainloop()
    map.cef.Shutdown()