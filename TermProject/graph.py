from tkinter import*
from math import*

class Graph:
    def __init__(self,frame,bg,cWidth,cHeight,data , x, y):
        # frame : 그래프를 그릴 프레임/윈도우
        # x/y : 그래프가 그려질 위치
        # cWidth / cHeight : 그래프이 길이/ 높이
        # data : [{itme : val}, ...] 형식의 데이터 묶음
        # bg : 캔버스의 배경색

        self.width = cWidth
        self.height =cHeight
        self.frame = frame

        # data를 list로 추출
        self.items = [i for i in data]
        self.vals = [eval(data[i]) for i in self.items]

        self.maxVal = sum(self.vals)


        # 캔버스 그리기
        self.canvas = Canvas(self.frame, bg=bg, width=cWidth, height=cHeight, bd=0)
        self.canvas.place(x=x, y=y)  # 이후 place 배치로 바꿀 수 있음

    def DrawVerticalGraph(self,sColors, tag ):
        # sWidth / sHeight : 막대바의 넓이/최대길이
        # fontstyle/ fsize : 캔버스의 폰트/폰트크기
        # sColors = [color , color, ...]의 item별 막대그래프의 색상리스트
        # tag: 캔버스의 tags

        sWidth = self.width/len(self.items)
        sHeight = self.height * 3/4
        # 막대그래프 그리기
        for i in range(len(self.items)):
            self.canvas.create_rectangle(5, 10 + 15 * i - 5, 15, 10 + 15 * i + 5,
                                         fill=colors[i], tags=tag)
            self.canvas.create_text(60, 10 + i * 15, text=str(self.items[i]), tags=tag)
            self.canvas.create_rectangle(10+sWidth * i , (1-self.vals[i] / self.maxVal)*(self.height-self.height*1/4),10+sWidth* (i+1),
                                         self.height ,fill = sColors[i],tags = tag)
            self.canvas.create_text( 10 +sWidth * i + sWidth/2 ,8 + (1-self.vals[i] / self.maxVal) * sHeight - 15,
                                     text = str(self.vals[i]), tags = tag)



    def DrawHorisontalGraph(self, sColors, tag):
        # sWidth / sHeight : 막대바의 최대넓이/ 길이
        # sColors = [color , color, ...]의 item별 막대그래프의 색상리스트
        # tag: 캔버스의 tags

        sWidth = self.width * 3/4
        sHeight = (self.height * 3/4 ) / len(self.items) - 5
        for i in range(len(self.items)):
            self.canvas.create_rectangle(5, 10 + 15 * i - 5, 15, 10 + 15 * i + 5,
                                         fill=colors[i], tags=tag)
            self.canvas.create_text(60, 10 + i * 15, text=str(self.items[i]), tags=tag)
            self.canvas.create_rectangle(30, self.height * 1/4 +15+ sHeight*i,self.vals[i]/self.maxVal * sWidth + 30,
                                         self.height * 1/4 +15 + sHeight*(i+1), fill = sColors[i], tags = tag)
            self.canvas.create_text(self.vals[i]/self.maxVal * sWidth + 30 + 10,self.height * 1/4 +15 + sHeight*i + sHeight/2,
                                    text = self.vals[i],tags= tag)

    def DrawCircleGraph(self ,r,sColors,tag):
        # r: 반지름
        # sColors = [color , color, ...]의 item별 막대그래프의 색상리스트
        # tag: 캔버스의 tags
        s = 0
        for i in range(len(self.items)):
            e = (self.vals[i] / sum(self.vals)) * 360
            self.canvas.create_rectangle(5 ,10 + 15 * i-5,15,10 + 15 * i+5,
                                         fill = colors[i],tags= tag)
            self.canvas.create_text(60, 10+i*15,text = str(self.items[i] + "\t" + str(self.vals[i])),tags= tag)
            self.canvas.create_arc(self.width/2 - r,self.height/2 - r, self.width/2 - r + 20+2*r, self.height/2 - r +2*r,
                                   start = s,extent = e,fill = colors[i],tags= tag)
            s +=e
        pass



