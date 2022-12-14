from tkinter import *
from tkinter import ttk


def addition():
    a = txt1_1.get()
    b = txt1_2.get()
    c = float(a) + float(b)
    lbl1_3.configure(text=c)


def subtraction():
    a = txt2_1.get()
    b = txt2_2.get()
    c = float(a) - float(b)
    lbl2_3.configure(text=c)


def multiplication():
    a = txt3_1.get()
    b = txt3_2.get()
    c = float(a) * float(b)
    lbl3_3.configure(text=c)


def division():
    a = txt4_1.get()
    b = txt4_2.get()
    c = float(a) / float(b)
    lbl4_3.configure(text=c)


window = Tk()
window.title("Калькулятор")
window.geometry('260x50')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Addition')
tab_control.add(tab2, text='Subtraction')
tab_control.add(tab3, text='Multiplication')
tab_control.add(tab4, text='Division')
lbl1_1 = Label(tab1, text='=')
lbl1_1.grid(column=4, row=0)
lbl1_2 = Label(tab1, text='+')
lbl1_2.grid(column=2, row=0)
lbl1_3 = Label(tab1, text=' ')
lbl1_3.grid(column=5, row=0)
txt1_1 = Entry(tab1, width=10)
txt1_1.grid(column=1, row=0)
txt1_2 = Entry(tab1, width=10)
txt1_2.grid(column=3, row=0)
btn1 = Button(tab1, text="Сложить!", command=addition)
btn1.grid(column=6, row=0)
lbl2_1 = Label(tab2, text='=')
lbl2_1.grid(column=4, row=0)
lbl2_2 = Label(tab2, text='-')
lbl2_2.grid(column=2, row=0)
lbl2_3 = Label(tab2, text=' ')
lbl2_3.grid(column=5, row=0)
txt2_1 = Entry(tab2, width=10)
txt2_1.grid(column=1, row=0)
txt2_2 = Entry(tab2, width=10)
txt2_2.grid(column=3, row=0)
btn2 = Button(tab2, text="Вычесть!", command=subtraction)
btn2.grid(column=6, row=0)
lbl3_1 = Label(tab3, text='=')
lbl3_1.grid(column=4, row=0)
lbl3_2 = Label(tab3, text='x')
lbl3_2.grid(column=2, row=0)
lbl3_3 = Label(tab3, text=' ')
lbl3_3.grid(column=5, row=0)
txt3_1 = Entry(tab3, width=10)
txt3_1.grid(column=1, row=0)
txt3_2 = Entry(tab3, width=10)
txt3_2.grid(column=3, row=0)
btn3 = Button(tab3, text="Умножить!", command=multiplication)
btn3.grid(column=6, row=0)
lbl4_1 = Label(tab4, text='=')
lbl4_1.grid(column=4, row=0)
lbl4_2 = Label(tab4, text='/')
lbl4_2.grid(column=2, row=0)
lbl4_3 = Label(tab4, text=' ')
lbl4_3.grid(column=5, row=0)
txt4_1 = Entry(tab4, width=10)
txt4_1.grid(column=1, row=0)
txt4_2 = Entry(tab4, width=10)
txt4_2.grid(column=3, row=0)
btn4 = Button(tab4, text="Разделить!", command=division)
btn4.grid(column=6, row=0)
tab_control.pack(expand=1, fill='both')
window.mainloop()
