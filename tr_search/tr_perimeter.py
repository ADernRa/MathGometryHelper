from tkinter import *
import clear
import math
import MainWin

def tr_perimeter(main_win):
    clear.ClearWin(main_win)

    canvas = Canvas(bg="black", width=300, height=300, highlightbackground = "black")
    canvas.place(anchor=CENTER, x=300, y= 240)
    canvas.create_polygon(150, 20, 20, 280, 280, 280, fill="black",outline="white")
    
    def validate(new_value):
        my_list = ['1','2','3','4','5','6','7','8','9','0','.']
        return all(c in my_list for c in new_value)
    
    vcmd = (main_win.register(validate), '%P')

    def start():
        if ent_AB.get() == '' or ent_AC.get() == '' or ent_BC.get() == '':
            error_str.set("Введите значения для сторон")
            return
        elif float(ent_AB.get()) == 0 or float(ent_AC.get()) == 0 or float(ent_BC.get()) == 0:
            error_str.set("Сторона должна быть больше за 0")
            return
        elif float(ent_AB.get()) > float(ent_AC.get())+float(ent_BC.get()) or float(ent_BC.get()) > float(ent_AC.get())+float(ent_AB.get()) or float(ent_AC.get()) > float(ent_BC.get())+float(ent_AB.get()):
            error_str.set("Триуголник не может существовать")
            return
        else:
            error_str.set("")
            BC = float(ent_BC.get())
            AB = float(ent_AB.get())
            AC = float(ent_AC.get())

            btn_back= Button(text="В начало", width=8, height=2, compound="top",  font=("Arial", 16), command=lambda: tr_perimeter(main_win))
            btn_back.place(anchor="c", y=130, x = 1000)

            lbl_info.destroy()
            btn_start.destroy()
            ent_BC.destroy()
            ent_AB.destroy()
            ent_AC.destroy()

            lbl_BC = Label(text=BC, bg="black", fg="white", font=["Arial", 14])
            lbl_BC.place(anchor=CENTER, x=395, y=230)

            lbl_AB = Label(text=AB, bg="black", fg="white", font=["Arial", 14])
            lbl_AB.place(anchor=CENTER,  x=205, y=230)

            lbl_AC = Label(text=AC, bg="black", fg="white", font=["Arial", 14])
            lbl_AC.place(anchor=CENTER, x=300, y=395)

            P = BC + AB + AC
            tr_type = "Триугольник "
            if BC == AB and AB == AC and AC == BC:
                tr_type = tr_type + "\nравносторонний "
            elif BC == AB or AB == AC or AC == BC:
                tr_type = "\npавнобедренный "
            
            max_side = max(AB, AC, BC)
            sides = [AB, AC, BC]
            check = False
            sidee = [0,0]
            i=0
            for side in sides:
                if side == max_side and check == False:
                    check = True
                elif side != max_side or check == True:
                    sidee[i] = side
                    i=1
            print(max_side, sidee[0], sidee[1])
            if pow(AB, 2) == pow(BC,2) + pow(AC, 2) or pow(BC, 2) == pow(AB,2) + pow(AC, 2) or pow(AC, 2) == pow(AB,2) + pow(BC, 2):
                tr_type = tr_type + "\nпрямоугольный"
            elif pow(max_side, 2) <  pow(sidee[1], 2) + pow(sidee[0], 2):
                tr_type = tr_type + "\nостроугольный"
            elif pow(max_side, 2) >  pow(sidee[1], 2) + pow(sidee[0], 2):
                tr_type = tr_type + "\nтупоугольный"

            lbl_teor = Label(justify=LEFT, font=["Arial", 22],bg="black", fg="White", text=f"P = AB + BC + AC\nP = {AB} + {BC} + {AC}\nP = {P}\n{tr_type}")
            lbl_teor.place( anchor=CENTER,x=700, y=200)
            
            lbl_per = Label(text=f"P = {P}", bg="black", fg="white", font=["Arial", 14])
            lbl_per.place(anchor=CENTER, x=300, y=270)


    error_str = StringVar()
    lbl_error = Label(textvariable=error_str, font=["Arial", 14], fg="red", bg="black")
    lbl_error.place(anchor=CENTER, x=285, y=520)
    
    lbl_info = Label(font=["Arial",14], bg="black", fg="White", text="Введите длину сторон триугольника")
    lbl_info.place(anchor=CENTER, x=300, y=40)

    lbl_B = Label(font=["Arial",14], bg="black", fg="White", text="B")
    lbl_B.place(anchor=CENTER, x=300,y=80)

    lbl_A = Label(font=["Arial",14], bg="black", fg="White", text="A")
    lbl_A.place(anchor=CENTER, x=150,y=380)

    lbl_C = Label(font=["Arial",14], bg="black", fg="White", text="C")
    lbl_C.place(anchor=CENTER, x=440,y=380)

    ent_AB = Entry(width=5, validate='key', validatecommand=vcmd)
    ent_AB.place(anchor=CENTER, x=205, y=230)

    ent_BC = Entry(width=5, validate='key', validatecommand=vcmd)
    ent_BC.place(anchor=CENTER, x=395, y=230)

    ent_AC = Entry(width=5, validate='key', validatecommand=vcmd)
    ent_AC.place(anchor=CENTER, x=300, y=395)

    btn_start = Button(text="Найти периметр",font=["Arial",14], width=15, height=2, command=start)
    btn_start.place(anchor=CENTER, x=285, y=470)
    
    btn_back= Button(text="В меню", width=8, height=2, compound="top",  font=("Arial", 16), command=lambda: MainWin.MainWin(main_win))
    btn_back.place(anchor="c", y=50, x = 1000)