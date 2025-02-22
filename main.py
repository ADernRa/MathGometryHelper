from tkinter import *
from PIL import ImageTk
main_win = Tk()

def ClearWin():
    for widget in main_win.winfo_children():
        widget.destroy()
    
def CreateWin():
    main_win.title("MathHelper")
    main_win.geometry("1080x540")
    main_win.resizable(False, False)
    main_win.config(bg="black")
    icon = PhotoImage(file = "icon.png")
    main_win.iconphoto(False, icon)

def MainWin():
    ClearWin()

    tr_side = ImageTk.PhotoImage(file = "MenuPng/tr_side.png")
    btn_tr_side= Button(text="Найти сторону",image=tr_side, width=140, height=150, compound="top",  font=("Arial", 16))
    btn_tr_side.place(anchor="c", y=130, x = 110)
    btn_tr_side_help= Button(text=" ? ", width=1, height=1,  font=("Arial", 16))
    btn_tr_side_help.place(anchor="c", y=73, x = 195)

    tr_corner = ImageTk.PhotoImage(file = "MenuPng/tr_corner.png")
    btn_tr_corner= Button(text="Найти угол",image=tr_corner, width=140, height=150, compound="top",  font=("Arial", 16))
    btn_tr_corner.place(anchor="c", y=130, x = 310)
    btn_tr_corner_help= Button(text=" ? ", width=1, height=1,  font=("Arial", 16))
    btn_tr_corner_help.place(anchor="c", y=73, x = 395)

    tr_area = ImageTk.PhotoImage(file = "MenuPng/tr_area.png")
    btn_tr_area = Button(text="Найти прощадь",image=tr_area, width=140, height=150, compound="top",  font=("Arial", 16))
    btn_tr_area.place(anchor="c", y=130, x = 510)
    btn_tr_area_help= Button(text=" ? ", width=1, height=1,  font=("Arial", 16))
    btn_tr_area_help.place(anchor="c", y=73, x = 595)

    tr_sincos = ImageTk.PhotoImage(file = "MenuPng/tr_sincos.png")
    btn_tr_sincos= Button(text="Найти сторону\n через угол",image=tr_sincos, width=140, height=150, compound="top",  font=("Arial", 16))
    btn_tr_sincos.place(anchor="c", y=130, x = 710)
    btn_tr_sincos_help= Button(text=" ? ", width=1, height=1,  font=("Arial", 16))
    btn_tr_sincos_help.place(anchor="c", y=73, x = 795)

    tr_perimeter = ImageTk.PhotoImage(file = "MenuPng/tr_perimeter.png")
    btn_tr_perimeter= Button(text="Найти\n периметр",image=tr_perimeter, width=140, height=150, compound="top",  font=("Arial", 16))
    btn_tr_perimeter.place(anchor="c", y=130, x = 910)
    btn_tr_perimeter_help= Button(text=" ? ", width=1, height=1,  font=("Arial", 16))
    btn_tr_perimeter_help.place(anchor="c", y=73, x = 995)



    calculator = ImageTk.PhotoImage(file = "MenuPng/calculator.png")
    btn_calculator= Button(text="Простой\n калькулятор",image=calculator, width=140, height=150, compound="top",  font=("Arial", 16))
    btn_calculator.place(anchor="c", y=330, x = 110)
    btn_calculator_help= Button(text=" ? ", width=1, height=1,  font=("Arial", 16))
    btn_calculator_help.place(anchor="c", y=273, x = 195)

    square_table = ImageTk.PhotoImage(file = "MenuPng/square_table.png")
    btn_square_table= Button(text="Таблица\n квадратов",image=square_table, width=140, height=150, compound="top",  font=("Arial", 16))
    btn_square_table.place(anchor="c", y=330, x = 310)
    btn_square_table_help= Button(text=" ? ", width=1, height=1,  font=("Arial", 16))
    btn_square_table_help.place(anchor="c", y=273, x = 395)

    corners = ImageTk.PhotoImage(file = "MenuPng/corners.png")
    btn_corners= Button(text="Таблица\nуглов",image=corners, width=140, height=150, compound="top",  font=("Arial", 16))
    btn_corners.place(anchor="c", y=330, x = 510)
    btn_corners_help= Button(text=" ? ", width=1, height=1,  font=("Arial", 16))
    btn_corners_help.place(anchor="c", y=273, x = 595)

    percent = ImageTk.PhotoImage(file = "MenuPng/percent.png")
    btn_percent= Button(text="Найти %\n от числа",image=percent, width=140, height=150, compound="top",  font=("Arial", 16))
    btn_percent.place(anchor="c", y=330, x = 710)
    btn_percent_help= Button(text=" ? ", width=1, height=1,  font=("Arial", 16))
    btn_percent_help.place(anchor="c", y=273, x = 795)

    derivative = ImageTk.PhotoImage(file = "MenuPng/derivative.png")
    btn_derivative = Button(text="Найти\n производную",image=derivative, width=140, height=150, compound="top",  font=("Arial", 16))
    btn_derivative.place(anchor="c", y=330, x = 910)
    btn_derivative_help= Button(text=" ? ", width=1, height=1,  font=("Arial", 16))
    btn_derivative_help.place(anchor="c", y=273, x = 995)

CreateWin()
MainWin()
main_win.mainloop()