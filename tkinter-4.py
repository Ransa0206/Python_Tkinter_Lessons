from tkinter import* 

win = Tk()
win.geometry('400x200')
win.config(bg='#222222')

#function
def Label_Change(): # 定義Label_Change
    if var.get() == '123': #當 字串變量 為 123 時執行 
         lb.config(text='This is a Good Label') #將Label的text 改為 This is a Good Label
       
    

#Label標籤
lb = Label(text="this is a Label") # 一樣可以設定BG FONT TEXT之類的
lb.pack()

#Entry輸入框+StringVar (Variavle = var 變量)
var = StringVar() #定義var為字串變量-StringVar
en = Entry(win , textvariable = var) #定義en為Entry ,輸入框所輸入的都為 字串變量
en.pack()

#Buttom
btn = Button(text="Finish") 
btn.config(command=Label_Change) #被點擊時觸發Label_Change
btn.pack()





win.mainloop()