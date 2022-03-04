from tkinter import*

win = Tk()
win.geometry('400x200')


#pack佈局
btn = Button(text='Buttom')
btn.pack(side='left') #左
btn = Button(text='Buttom')
btn.pack(side='right') #右
btn = Button(text='Buttom')
btn.pack(side='top') #上
btn = Button(text='Buttom')
btn.pack(side='bottom') #下



win.mainloop()