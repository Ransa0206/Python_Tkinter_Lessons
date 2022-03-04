from tkinter import*

win = Tk()
win.geometry('400x200')


def change(self):
    s_value = s.get() #s_value ＝ 抓取到的數值
    dv.config(text=s_value) #讓Label的text為s_value
    win.attributes('-alpha' ,s_value/100) #讓視窗的透明度數值設定為s_value的一百分之一 

    


s = Scale(orient=HORIZONTAL, length=200,width=15)  #orient 方向設定 = HORIZONTAL水平  /  VERTICAL垂直
s.config(from_=10, to = 100) #最大值到最小值

s.config(showvalue=False) #showvalue是否顯示數值
s.config(tickinterval=10) #tickinterval控制區間
s.config(resolution=10) #resolution每次的最小移動量
s.config(digits=5) #digits最高位數顯示
#可以簡化成  s.config(showvalue=False,tickinterval=5,resolution=10,digits=5)
s.set(100) #初始化數值 
s.config(command=change)
s.config(label="A Slider") #設定LABEL名稱為A Slider
s.pack()

#Label
dv = Label()
dv.pack(side=BOTTOM)
dv.config(text='100.0')


win.mainloop()