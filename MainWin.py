import clear
from tkinter import *
from PIL import ImageTk
import alg_search.square_table as square_table
import alg_search.calculator as calculator
import tr_search.tr_side as tr_side
import tr_search.tr_corner as tr_corner
import tr_search.tr_perimeter as tr_perimeter

def MainWin(main_win):
    clear.ClearWin(main_win)

    tr_side_img = ImageTk.PhotoImage(file = "MenuPng/tr_side.png")
    btn_tr_side= Button(text="Найти сторону",image=tr_side_img, width=140, height=150, compound="top",  font=("Arial", 16), command=lambda: tr_side.tr_side(main_win))
    btn_tr_side.place(anchor="c", y=130, x = 110)

    tr_corner_img = ImageTk.PhotoImage(file = "MenuPng/tr_corner.png")
    btn_tr_corner= Button(text="Найти угол",image=tr_corner_img, width=140, height=150, compound="top",  font=("Arial", 16), command=lambda: tr_corner.tr_corner(main_win))
    btn_tr_corner.place(anchor="c", y=130, x = 310)

    tr_area = ImageTk.PhotoImage(file = "MenuPng/tr_area.png")
    btn_tr_area = Button(text="Найти прощадь",image=tr_area, width=140, height=150, compound="top",  font=("Arial", 16))
    btn_tr_area.place(anchor="c", y=130, x = 510)

    tr_sincos = ImageTk.PhotoImage(file = "MenuPng/tr_sincos.png")
    btn_tr_sincos= Button(text="Найти сторону\n через угол",image=tr_sincos, width=140, height=150, compound="top",  font=("Arial", 16))
    btn_tr_sincos.place(anchor="c", y=130, x = 710)

    tr_perimeter_img = ImageTk.PhotoImage(file = "MenuPng/tr_perimeter.png")
    btn_tr_perimeter= Button(text="Найти\n периметр",image=tr_perimeter_img, width=140, height=150, compound="top",  font=("Arial", 16),command=lambda: tr_perimeter.tr_perimeter(main_win))
    btn_tr_perimeter.place(anchor="c", y=130, x = 910)



    calculator_img = ImageTk.PhotoImage(file = "MenuPng/calculator.png")
    btn_calculator= Button(text="Простой\n калькулятор",image=calculator_img, width=140, height=150, compound="top",  font=("Arial", 16), command=lambda: calculator.calculator(main_win))
    btn_calculator.place(anchor="c", y=330, x = 110)

    square_table_img = ImageTk.PhotoImage(file = "MenuPng/square_table.png")
    btn_square_table= Button(text="Таблица\n квадратов",image=square_table_img, width=140, height=150, compound="top",  font=("Arial", 16), command=lambda: square_table.square_table(main_win))
    btn_square_table.place(anchor="c", y=330, x = 310)

    corners = ImageTk.PhotoImage(file = "MenuPng/corners.png")
    btn_corners= Button(text="Таблица\nуглов",image=corners, width=140, height=150, compound="top",  font=("Arial", 16))
    btn_corners.place(anchor="c", y=330, x = 510)

    percent = ImageTk.PhotoImage(file = "MenuPng/percent.png")
    btn_percent= Button(text="Найти %\n от числа",image=percent, width=140, height=150, compound="top",  font=("Arial", 16))
    btn_percent.place(anchor="c", y=330, x = 710)

    derivative = ImageTk.PhotoImage(file = "MenuPng/derivative.png")
    btn_derivative = Button(text="Найти\n производную",image=derivative, width=140, height=150, compound="top",  font=("Arial", 16))
    btn_derivative.place(anchor="c", y=330, x = 910)