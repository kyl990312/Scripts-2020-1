from tkinter import*
import subprocess
import os
import io
from tkinter import filedialog

from PIL import Image
import turtle


class Graph:
    def __init__(self,frame,bg,cWidth,cHeight , x, y,fileName):
        # frame : 그래프를 그릴 프레임/윈도우
        # x/y : 그래프가 그려질 위치
        # cWidth / cHeight : 그래프이 길이/ 높이
        # data : [{itme : val}, ...] 형식의 데이터 묶음
        # bg : 캔버스의 배경색

        self.width = cWidth
        self.height =cHeight
        self.frame = frame
        self.items = []
        self.vals = []
        self.maxVal = 0

        # 캔버스 그리기
        self.canvas = Canvas(self.frame, bg=bg, width=cWidth, height=cHeight,bd = 0, highlightthickness = 0)
        self.canvas.place(x=x, y=y)  # 이후 place 배치로 바꿀 수 있음

        # Email 전송시 필요한 그래프 image
        self.fileName = fileName

    def SetData(self,data):
        # data를 list로 추출
        self.items.clear()
        for i in data:
            self.items.append(i)
        self.vals.clear()
        for i in data:
            self.vals.append(eval(data[i]))
        self.maxVal = sum(self.vals)

    def DrawVerticalGraph(self,sColors, tag ):
        self.fileName += '_VerticalGraph.jpg'
        # sWidth / sHeight : 막대바의 넓이/최대길이
        # fontstyle/ fsize : 캔버스의 폰트/폰트크기
        # sColors = [color , color, ...]의 item별 막대그래프의 색상리스트
        # tag: 캔버스의 tags
        self.canvas.delete(tag)
        sWidth = self.width/len(self.items)
        sHeight = self.height * 3/4
        # 막대그래프 그리기
        for i in range(len(self.items)):
            self.canvas.create_rectangle(5, 10 + 15 * i - 5, 15, 10 + 15 * i + 5,
                                         fill=sColors[i], tags=tag)
            self.canvas.create_text(60, 10 + i * 15, text=str(self.items[i]), tags=tag)
            self.canvas.create_rectangle(10+sWidth * i , (1-self.vals[i] / self.maxVal)*(self.height-self.height*1/4),10+sWidth* (i+1),
                                         self.height ,fill = sColors[i],tags = tag)
            self.canvas.create_text( 10 +sWidth * i + sWidth/2 ,8 + (1-self.vals[i] / self.maxVal) * sHeight - 15,
                                     text = str(self.vals[i]), tags = tag)



    def DrawHorisontalGraph(self, sColors, tag):
        self.fileName += '_HorizontalGraph.jpg'
        self.canvas.delete(tag)
        # sWidth / sHeight : 막대바의 최대넓이/ 길이
        # sColors = [color , color, ...]의 item별 막대그래프의 색상리스트
        # tag: 캔버스의 tags

        sWidth = self.width * 3/4
        sHeight = self.height/5
        smallSize = (self.height * 1/8)
        if smallSize > 10:
            smallSize = 10
        startY = 15 +smallSize * len(self.items)
        beforeX = 30

        for i in range(len(self.items)):
            thisWid = self.vals[i]/self.maxVal * sWidth
            self.canvas.create_rectangle(5, 5 + smallSize * i, smallSize + 5, 5 + smallSize * (i+1),
                                         fill=sColors[i], tags=tag)
            self.canvas.create_text(60,  5 + smallSize * i +smallSize/2 , text=str(self.items[i]), tags=tag)
            self.canvas.create_rectangle(beforeX, startY, beforeX + thisWid,startY + sHeight, fill = sColors[i], tags = tag)
            self.canvas.create_text(beforeX + thisWid/2,startY + sHeight + 10, text = self.vals[i],tags= tag)
            beforeX += thisWid

    def DrawCircleGraph(self ,sColors,tag):
        self.fileName += '_CircleGraph.jpg'
        self.canvas.delete(tag)
        # r: 반지름
        # sColors = [color , color, ...]의 item별 막대그래프의 색상리스트
        # tag: 캔버스의 tags
        s = 0
        smallSize = (self.height * 1 / 20)
        if smallSize > 10:
            smallSize = 10
        startY = 15 + smallSize * len(self.items)
        r = (self.height - startY - 10)/2
        for i in range(len(self.items)):
            e = (self.vals[i] / sum(self.vals)) * 360
            self.canvas.create_rectangle( 5,10 + smallSize * i ,smallSize + 5,10 + smallSize * (i+1),
                                         fill = sColors[i],tags= tag)
            self.canvas.create_text(5 +smallSize + self.width / 3, 10 + smallSize * i + smallSize/2,text = str(self.items[i] + "  " + str(self.vals[i])),
                                    tags= tag)
            self.canvas.create_arc(self.width/2 - r,startY, self.width/2 + r , startY + 2*r,
                                   start = s,extent = e,fill = sColors[i],tags= tag)
            s += e
        pass

    def ConvertCanvasToImage(self):
        #ps = self.canvas.postscript(colormode='color')
        ##self.fileName = filedialog.asksaveasfilename(defaultextension='.png')
        #im = Image.open(io.BytesIO(ps.encode('utf-8')))
        #im.write( self.fileName + '.png')
        pass


#window = Tk()
#frame = Frame(window,width = 400,height = 400)
#frame.pack()
#data = {"안녕":'10',"반가워":'20',"김정윤":'40',"멍청이":'30'}
#color = ['gray','red','blue','orange']
#g = Graph(frame,'white',400,400,data,0,0,"test")
#g.DrawCircleGraph(100,color,"babo")
#g.ConvertCanvasToImage()
#window.mainloop()



