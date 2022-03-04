from re import L
from tkinter import*

win = Tk()
win.title('tkinter gui')
win.geometry('400x200+500+500')

#Grid網格佈局  row 列(橫)  column行(直)

#Label
user = Label(text='User:')
user.grid(row=0, column=0)

password = Label(text='Password:') 
password.grid(row=1, column=0)

#輸入框
userEn = Entry() #可透過（font='Arial' , 12）調整輸入框的大小
userEn.grid(row=0, column=1)  

passwordEn = Entry()
passwordEn.grid(row=1 , column=1) 

TestEn = Entry(font=('DisposableDroid BB',16))
TestEn.grid(row=3, column=0, columnspan=4) # rowspan / columnspan 設定跨格





win.mainloop()