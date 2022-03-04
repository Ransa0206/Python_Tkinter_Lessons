from tkinter import*

win = Tk()
win.geometry('400x400')

#place佈局
btn = Button(text='Buttom')
btn.place(x=100 , y=100,anchor=CENTER)#x y座標 anchor方位


win.mainloop()