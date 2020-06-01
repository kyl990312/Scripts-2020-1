from tkinter import *

def pressed(X):
    frames[X].tkraise()

window = Tk()
frame0 = Frame(window)
frame0.grid(row=1,column=2)
frames=[]

#학과 이름
Label(window, text="학과 이름", width=15).grid(row=0, column=0)
#학과 이름 입력
Entry(window, width=15).grid(row=1, column=0)
#학과 이름 입력 후 오케이 버튼
Button(window, text="OK", width=5).grid(row=1, column=1)
#학교 이름
Label(window, text="해당 과가 있는 학교", width=15).grid(row=2, column=0)

# 프레임
# 프레임 1 : 학교 정보
# 프레임 2 : 학과 정보
# 프레임 3 : 취업 정보
for i in range(3):
    Button(frame0,text="Frame"+str(i),command=lambda X=i: pressed(X)).pack(side=LEFT)
    frames.append(Frame(window))
    frames[i].grid(row=3,column=2)
    label = Label(frames[i],text="FRAME"+str(i),width=10,height=10)
    label.pack()

window.mainloop()