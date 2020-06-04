from tkinter import *
from loading import Data

class MainGUI:
    def __init__(self):
        self.datas = Data()              # 검색하는 학과의 정보를 담는다.

        self.window = Tk()

        self.frame0 = Frame(self.window)
        self.frame0.grid(row=1, column=2)
        self.frames = []

        # 학과 이름
        Label(self.window, text="학과 이름", width=15).grid(row=0, column=0)
        # 학과 이름 입력
        self.major = Entry(self.window, width=15)
        self.major .grid(row=1, column=0)
        # 학과 이름 입력 후 오케이 버튼
        Button(self.window, text="OK", width=5, command= self.OKProcess).grid(row=1, column=1)
        # 학교 이름
        Label(self.window, text="해당 과가 있는 학교", width=15).grid(row=2, column=0)

        # 프레임
        # 프레임 1 : 학교 정보
        # 프레임 2 : 학과 정보
        # 프레임 3 : 취업 정보
        for i in range(3):
            Button(self.frame0, text="Frame" + str(i), command=lambda X=i: self.pressed(X)).pack(side=LEFT)
            self.frames.append(Frame(self.window))
            self.frames[i].grid(row=3, column=2)
            label = Label(self.frames[i], text="FRAME" + str(i), width=10, height=10)
            label.pack()

        self.window.mainloop()

    def pressed(self,X):
        self.frames[X].tkraise()

    def OKProcess(self):
        self.datas.Loading(self.major.get())              # 학과에 해당하는 정보를 만든다

MainGUI()

