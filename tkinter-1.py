import tkinter as tk
import tkinter as tk #導入ＴＫ函式庫

window = tk.Tk() #設定標題

window.title('tkinter gui') #視窗名稱

window.geometry('600x800') #視窗大小

lbl_1 = tk.Label(window, text='hellow world', bg='yellow', fg='#000000', font=('DisposableDroid BB','16')) #讓lbl_1 = tk.Label 跟設定

lbl_1.grid(column=0, row=0) #放置的位置

window.mainloop() #主視窗開啟