from tkinter import *
from tkinter.ttk import *

# 定义事件范围
yearitems = ("2022", "2023", "2024", "2025")
monthitems = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")

# 生成窗口
root = Tk()
root.title("住户地方点数据汇总系统")
root.geometry("1024x768")
root.resizable(TRUE, TRUE)

# 生成选择时间按钮
lable1 = Label(root, text='请选择时间')
lable1.grid(row=0, column=0)
yearchoice = Combobox(root)
yearchoice.grid(row=0, column=1)
yearchoice['values'] = yearitems
monthchoice = Combobox(root)
monthchoice.grid(row=1, column=1)
monthchoice['values'] = monthitems


# 定义生成子程序
def show_click():
    year_var: str = yearchoice.get()
    return year_var


SC_botton = Button(root, text='生成数据', command=show_click)
SC_botton.grid(row=4, column=1)

root.mainloop()
