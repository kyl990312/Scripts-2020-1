from tkinter import *
from loading import Data

class MainGUI:
    def __init__(self):
        self.datas = Data()              # 검색하는 학과의 정보를 담는다.

        self.window = Tk()
        self.MajorFrame = Frame(self.window)
        self.MajorFrame.grid(row = 0,column = 0)
        self.UniFrame =Frame(self.window)
        self.UniFrame.grid(row = 1,column = 0)
        self.frame0 = Frame(self.window)
        self.frame0.grid(row=0, column=1)
        self.frames = []
        # 학과 이름 입력
        Label(self.MajorFrame, text="학과 이름", width=15).grid(row=0, column=0)
        self.major = Entry(self.MajorFrame, width=15)
        self.major.grid(row=1, column=0)
        # 학과 이름 입력 후 오케이 버튼
        Button(self.MajorFrame, text="OK", width=5, command= self.OKProcess).grid(row=1, column=1)

        # 지역 분류 : 0.서울 특별시, 1. 수도권: 경기도 + 인천, 2. 충청도, 3. 강원도, 4. 전라도 + 광주 + 대전, 5. 경상도 + 대구 + 부산, 6.제주특별자치구
        Label(self.UniFrame, text = "지역", width = 15).grid(row = 2, column =0)

        self.checkVal0 = IntVar()
        self.checkVal1 = IntVar()
        self.checkVal2 = IntVar()
        self.checkVal3 = IntVar()
        self.checkVal4 = IntVar()
        self.checkVal5 = IntVar()
        self.checkVal6 = IntVar()
        self.checkList = [Checkbutton(self.UniFrame, variable = self.checkVal0, width = 5, height = 1,  text = "서울"),
                          Checkbutton(self.UniFrame, variable = self.checkVal1, width = 5, height = 1, text = "수도권"),
                          Checkbutton(self.UniFrame, variable = self.checkVal2, width = 5, height = 1, text = "충청도"),
                          Checkbutton(self.UniFrame, variable = self.checkVal3, width = 5, height = 1, text = "강원도"),
                          Checkbutton(self.UniFrame, variable = self.checkVal4, width = 15, height = 1, text = "전라도,광주,대전"),
                          Checkbutton(self.UniFrame, variable = self.checkVal5, width = 15, height = 1, text = "경상도,대구,부산"),
                          Checkbutton(self.UniFrame, variable = self.checkVal6, width = 5, height = 1, text = "제주")]
        self.checkList[0].grid(row = 3, column = 0)
        self.checkList[1].grid(row=3, column=1)
        self.checkList[2].grid(row=4, column=0)
        self.checkList[3].grid(row=4, column=1)
        self.checkList[4].grid(row=5, column=0)
        self.checkList[5].grid(row=6, column=0)
        self.checkList[6].grid(row=7, column=0)


        # 학교 이름
        Label(self.UniFrame, text="해당 과가 있는 학교", width=15,height = 1).grid(row=8, column=0)
        self.listbox = Listbox(self.UniFrame,width = 15, height = 30)
        self.listbox.grid(row = 9, column = 0)


        # 프레임
        # 프레임 1 : 학교 정보
        # 프레임 2 : 학과 정보
        # 프레임 3 : 취업 정보
        for i in range(3):
            Button(self.frame0, text="Frame" + str(i), command=lambda X=i: self.pressed(X)).pack(side=LEFT)
            self.frames.append(Frame(self.window))
            self.frames[i].grid(row=1, column=1)
            label = Label(self.frames[i], text="FRAME" + str(i), width=60, height=30)
            label.pack()

        self.window.mainloop()

    def pressed(self,X):
        self.frames[X].tkraise()
        if X == 0:
            pass
        if X == 1:
            pass
        if X == 2:
            pass

    def OKProcess(self):
        self.datas.MakeUniversityData(self.major.get())              # 학과에 해당하는 대학정보를 만든다
        self.InputUniVersityToList()

    def InputUniVersityToList(self):
        applicableList = []
        idx = 0




MainGUI()

