from tkinter import *
import clear
import math
import MainWin

def tr_corner(main_win):
    clear.ClearWin(main_win)

    canvas = Canvas(bg="black", width=300, height=300, highlightbackground = "black")
    canvas.place(anchor=CENTER, x=300, y= 240)
    canvas.create_polygon(150, 20, 20, 280, 280, 280, fill="black",outline="white")

    def validate(new_value):
        my_list = ['1','2','3','4','5','6','7','8','9','0','.']
        return all(c in my_list for c in new_value)
    
    vcmd = (main_win.register(validate), '%P')
    
    lbl_info = Label(font=["Arial",14], bg="black", fg="White", text="Выберите угол который необходимо найти")
    lbl_info.place(anchor=CENTER, x=300, y=40)

    lbl_B = Label(font=["Arial",14], bg="black", fg="White", text="B")
    lbl_B.place(anchor=CENTER, x=300,y=80)

    lbl_A = Label(font=["Arial",14], bg="black", fg="White", text="A")
    lbl_A.place(anchor=CENTER, x=150,y=380)

    lbl_C = Label(font=["Arial",14], bg="black", fg="White", text="C")
    lbl_C.place(anchor=CENTER, x=440,y=380)

    btn_B = Button(width=5, height=2, text="B")
    btn_B.place(anchor=CENTER, x=300,y=80)

    btn_C = Button(width=5, height=2, text="C")
    btn_C.place(anchor=CENTER,  x=440,y=380)

    btn_A = Button(width=5, height=2, text="A")
    btn_A.place(anchor=CENTER, x=150,y=380) 

    btn_back= Button(text="В меню", width=8, height=2, compound="top",  font=("Arial", 16), command=lambda: MainWin.MainWin(main_win))
    btn_back.place(anchor="c", y=50, x = 1000)