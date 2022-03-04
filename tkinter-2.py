import tkinter as tk

window = tk.Tk()
window.title('tkinter gui')

#視窗大小控制
window.geometry('200x200+500+500') # 初始化狀態的視窗 , +X +Y 為螢幕實際座標
window.minsize(width=200, height=200) # 可調整視窗大小的最小值
window.maxsize(width=1024, height=768) #可調整視窗大小的最大值

window.resizable(False,False) #是否能手動調整視窗大小
# False = 0 ,True=1

#ICON 
window.iconbitmap('')  #.ico 建議使用完整路徑

#BackGroundColor
window.config(background="red")  # background = bg 可使用顏色的代碼

#透明度
window.attributes("-alpha", 0.5)  #1~0   |  1 = 100%  0 = 0%

#置頂
window.attributes("-topmost", True) # False = 0 ,True=1

window.mainloop()