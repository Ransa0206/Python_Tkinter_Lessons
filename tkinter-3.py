from tkinter import* #更簡單的導入方式 可以讓程式碼更簡潔

win = Tk()
win.title('tkinter gui')
win.geometry('400x200')

#image  （程式碼是從上往下讀如果要使用檔案或圖片盡量在上面就設定好)
img = PhotoImage(file="") #建議使用完整路徑 

#function
def say_hi():
    print("Hi!")

#Button = btn
btn = Button(text="click")
btn.config(bg='red', width=20,height=20, font=('DisposableDroid BB',16)) #利用配置-Config設定  （MAC系統上不會顯示顏色
btn.config(image=img) #設定圖片
btn.config(command=say_hi) #配置觸發後的指令-command
btn.pack() #放置按鈕 



win.mainloop()
