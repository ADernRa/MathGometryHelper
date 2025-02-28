from tkinter import *
import clear
import math
import MainWin

def tr_side(main_win):
    clear.ClearWin(main_win)
    
    canvas = Canvas(bg="black", width=300, height=300, highlightbackground = "black")
    canvas.place(anchor=CENTER, x=300, y= 240)
    canvas.create_polygon(20, 20, 20, 280, 280, 280, fill="black",outline="white")

    def validate(new_value):
        my_list = ['1','2','3','4','5','6','7','8','9','0','.']
        return all(c in my_list for c in new_value)
    
    vcmd = (main_win.register(validate), '%P')



    def search_AC():
        lbl_info["text"] = "Введіть довжину сторін"
        btn_BC.destroy()
        btn_AC.destroy()
        btn_AB.destroy()

        entry_BC = Entry(width=5, validate='key', validatecommand=vcmd)
        entry_BC.place(anchor=CENTER, x=280, y=400)

        entry_AB = Entry(width=5, validate='key', validatecommand=vcmd)
        entry_AB.place(anchor=CENTER, x=350, y=230)
        
        btn_back= Button(text="В начало", width=8, height=2, compound="top",  font=("Arial", 16), command=lambda: tr_side(main_win))
        btn_back.place(anchor="c", y=130, x = 1000)

        def start():
            if entry_AB.get() == '' or entry_BC.get() == '':
                error_str.set("Необходимо ввести значение")
                return
            elif float(entry_AB.get()) == 0 or float(entry_BC.get()) == 0:
                error_str.set("Сторона должна быть больше за 0")
                return
            elif float(entry_AB.get())<float(entry_BC.get()):
                error_str.set("Гипотинуза не может быть короче катета")
                return
            else:
                error_str.set("")
                AB = float(entry_AB.get())
                BC = float(entry_BC.get())

                entry_AB.destroy()
                entry_BC.destroy()
                btn_start.destroy()

                lbl_BC = Label(text=BC,font=["Arial", 14], fg="white", bg="black")
                lbl_BC.place(anchor=CENTER, x=280, y=400)

                lbl_AB = Label(text=AB,font=["Arial", 14], fg="white", bg="black")
                lbl_AB.place(anchor=CENTER, x=350, y=230)

                AC = round(math.sqrt(pow(AB, 2)-pow(BC, 2)),2)
                lbl_AC = Label(text=AC,font=["Arial", 14], fg="white", bg="black")
                lbl_AC.place(anchor=CENTER, x=140, y=250)

                lbl_teor = Label(justify=LEFT, font=["Arial", 22],bg="black", fg="White", text=f"AC = √(AB²-BC²)\nAC = √({AB}²-{BC}²)\nAC = √({pow(AB,2)}-{pow(BC,2)})\nAC = √{pow(AB,2)-pow(BC,2)}\nAC = {AC}")
                lbl_teor.place( anchor=CENTER,x=700, y=200)

        btn_start = Button(text="Знайти сторону",font=["Arial",14], width=15, height=2, command=start)
        btn_start.place(anchor=CENTER, x=285, y=470)

        error_str = StringVar()
        lbl_error = Label(textvariable=error_str, font=["Arial", 14], fg="red", bg="black")
        lbl_error.place(anchor=CENTER, x=285, y=520)



    def search_BC():
        lbl_info["text"] = "Введіть довжину сторін"
        btn_BC.destroy()
        btn_AC.destroy()
        btn_AB.destroy()

        entry_AC = Entry(width=5, validate='key', validatecommand=vcmd)
        entry_AC.place(anchor=CENTER, x=140, y=250)

        entry_AB = Entry(width=5, validate='key', validatecommand=vcmd)
        entry_AB.place(anchor=CENTER, x=350, y=230)

        btn_back= Button(text="В начало", width=8, height=2, compound="top",  font=("Arial", 16), command=lambda: tr_side(main_win))
        btn_back.place(anchor="c", y=130, x = 1000)

        def start():
            if entry_AB.get() == '' or entry_AC.get() == '':
                error_str.set("Необходимо ввести значение")
                return
            elif float(entry_AB.get()) == 0 or float(entry_AC.get()) == 0:
                error_str.set("Сторона должна быть больше за 0")
                return
            elif float(entry_AB.get())<float(entry_AC.get()):
                error_str.set("Гипотинуза не может быть короче катета")
                return
            else:
                error_str.set("")
                AB = float(entry_AB.get())
                AC = float(entry_AC.get())
            
                entry_AB.destroy()
                entry_AC.destroy()
                btn_start.destroy()

                lbl_AC = Label(text=AC,font=["Arial", 14], fg="white", bg="black")
                lbl_AC.place(anchor=CENTER, x=140, y=250)

                lbl_AB = Label(text=AB,font=["Arial", 14], fg="white", bg="black")
                lbl_AB.place(anchor=CENTER, x=350, y=230)

                BC = round(math.sqrt(pow(AB, 2)-pow(AC, 2)),2)
                lbl_BC = Label(text=BC,font=["Arial", 14], fg="white", bg="black")
                lbl_BC.place(anchor=CENTER, x=280, y=400)

                lbl_teor = Label(justify=LEFT, font=["Arial", 22],bg="black", fg="White", text=f"BC = √(AB²-AC²)\nBC = √({AB}²-{AC}²)\nBC = √({pow(AB,2)}-{pow(AC,2)})\nBC = √{pow(AB,2)-pow(AC,2)}\nBC = {BC}")
                lbl_teor.place( anchor=CENTER,x=700, y=200)

        btn_start = Button(text="Знайти сторону",font=["Arial",14], width=15, height=2, command=start)
        btn_start.place(anchor=CENTER, x=285, y=470)

        error_str = StringVar()
        lbl_error = Label(textvariable=error_str, font=["Arial", 14], fg="red", bg="black")
        lbl_error.place(anchor=CENTER, x=285, y=520)

    def search_AB():
        lbl_info["text"] = "Введите длину сторон"
        btn_BC.destroy()
        btn_AC.destroy()
        btn_AB.destroy()

        entry_AC = Entry(width=5, validate='key', validatecommand=vcmd)
        entry_AC.place(anchor=CENTER, x=140, y=250)

        entry_BC = Entry(width=5, validate='key', validatecommand=vcmd)
        entry_BC.place(anchor=CENTER, x=280, y=400)

        btn_back= Button(text="В начало", width=8, height=2, compound="top",  font=("Arial", 16), command=lambda: tr_side(main_win))
        btn_back.place(anchor="c", y=130, x = 1000)

        def start():
            if entry_BC.get() == '' or entry_AC.get() == '':
                error_str.set("Необходимо ввести значение")
                return
            elif float(entry_BC.get()) == 0 or float(entry_AC.get()) == 0:
                error_str.set("Сторона должна быть больше за 0")
                return
            else:
                error_str.set("")
                BC = float(entry_BC.get())
                AC = float(entry_AC.get())
                entry_BC.destroy()
                entry_AC.destroy()
                btn_start.destroy()

                lbl_AC = Label(text=AC,font=["Arial", 14], fg="white", bg="black")
                lbl_AC.place(anchor=CENTER, x=140, y=250)

                lbl_BC = Label(text=BC,font=["Arial", 14], fg="white", bg="black")
                lbl_BC.place(anchor=CENTER, x=280, y=400)

                AB = round(math.sqrt(pow(BC, 2)+pow(AC, 2)),2)
                lbl_AB = Label(text=AB,font=["Arial", 14], fg="white", bg="black")
                lbl_AB.place(anchor=CENTER, x=350, y=230)

                lbl_teor = Label(justify=LEFT, font=["Arial", 22],bg="black", fg="White", text=f"AB = √(BC²+AC²)\nAB = √({BC}²+{AC}²)\nAB = √({pow(BC,2)}+{pow(AC,2)})\nAB = √{pow(BC,2)+pow(AC,2)}\nAB = {AB}")
                lbl_teor.place( anchor=CENTER,x=700, y=200)

        btn_start = Button(text="Знайти сторону",font=["Arial",14], width=15, height=2, command=start)
        btn_start.place(anchor=CENTER, x=285, y=470)

        error_str = StringVar()
        lbl_error = Label(textvariable=error_str, font=["Arial", 14], fg="red", bg="black")
        lbl_error.place(anchor=CENTER, x=285, y=520)

    lbl_info = Label(font=["Arial",14], bg="black", fg="White", text="Выберите сторону которую необходимо найти")
    lbl_info.place(anchor=CENTER, x=300, y=40)

    lbl_A = Label(font=["Arial",14], bg="black", fg="White", text="A")
    lbl_A.place(anchor=CENTER, x=150,y=100)

    lbl_C = Label(font=["Arial",14], bg="black", fg="White", text="C")
    lbl_C.place(anchor=CENTER, x=150,y=380)

    lbl_B = Label(font=["Arial",14], bg="black", fg="White", text="B")
    lbl_B.place(anchor=CENTER, x=430,y=385)

    btn_AC = Button(text="AC", width=5, height=2, command=search_AC)
    btn_AC.place(anchor=CENTER, x=140, y=250)

    btn_BC = Button(text="BC", width=5, height=2, command=search_BC)
    btn_BC.place(anchor=CENTER, x=280, y=400)

    btn_AB = Button(text="AB", width=5, height=2, command=search_AB)
    btn_AB.place(anchor=CENTER, x=350, y=230)

    btn_back= Button(text="В меню", width=8, height=2, compound="top",  font=("Arial", 16), command=lambda: MainWin.MainWin(main_win))
    btn_back.place(anchor="c", y=50, x = 1000)