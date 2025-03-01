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
    
    def search(corner: str):
        lbl_info["text"] = "Введите чему равны углы"
        btn_A.destroy()
        btn_C.destroy()
        btn_B.destroy()

        btn_back= Button(text="В начало", width=8, height=2, compound="top",  font=("Arial", 16), command=lambda: tr_corner(main_win))
        btn_back.place(anchor="c", y=130, x = 1000)

        def start(cor1_entry: Entry, cor2_entry: Entry):
            if cor1_entry.get() == '' or cor2_entry.get() == '':
                error_str.set("Необходимо ввести значение")
                return
            elif float(cor1_entry.get()) == 0 or float(cor2_entry.get()) == 0:
                error_str.set("Угол должен быть больше за 0")
                return
            elif float(cor1_entry.get())+float(cor2_entry.get())>=180:
                error_str.set("Сумма двух углов должна быть меньше 180")
                return
            else:
                error_str.set("")
                cor1 = float(cor1_entry.get())
                cor2 = float(cor2_entry.get())
                cor1_entry.destroy()
                cor2_entry.destroy()
                btn_start.destroy()
                lbl_info.destroy()
                if corner == 'A':
                    lbl_B = Label(font=["Arial", 14], fg="white", bg="black", text=cor1)
                    lbl_B.place(anchor=CENTER, x=340,y=80)

                    lbl_C = Label(font=["Arial", 14], fg="white", bg="black", text=cor2)
                    lbl_C.place(anchor=CENTER,  x=480,y=380)

                    cor3 = 180-cor2-cor1
                    lbl_A = Label(font=["Arial", 14], fg="white", bg="black", text=cor3)
                    lbl_A.place(anchor=CENTER,  x=200,y=380)

                    lbl_teor = Label(justify=LEFT, font=["Arial", 22],bg="black", fg="White", text=f"∠A = 180 - (∠B+∠C) \n∠A = 180 - ({cor1} + {cor2})\n∠A = 180 - {cor1+cor2}\n∠A = {cor3}")
                    lbl_teor.place( anchor=CENTER,x=700, y=200)
                 
                elif corner == 'B':
                    lbl_A = Label(font=["Arial", 14], fg="white", bg="black", text=cor1)
                    lbl_A.place(anchor=CENTER, x=200,y=380)

                    lbl_C = Label(font=["Arial", 14], fg="white", bg="black", text=cor2)
                    lbl_C.place(anchor=CENTER,  x=480,y=380)

                    cor3 = 180-cor2-cor1
                    lbl_B = Label(font=["Arial", 14], fg="white", bg="black", text=cor3)
                    lbl_B.place(anchor=CENTER,  x=340,y=80)

                    lbl_teor = Label(justify=LEFT, font=["Arial", 22],bg="black", fg="White", text=f"∠B = 180 - (∠A+∠C) \n∠B = 180 - ({cor1} + {cor2})\n∠B = 180 - {cor1+cor2}\n∠B = {cor3}")
                    lbl_teor.place( anchor=CENTER,x=700, y=200)
                
                elif corner == 'C':
                    lbl_A = Label(font=["Arial", 14], fg="white", bg="black", text=cor1)
                    lbl_A.place(anchor=CENTER, x=200,y=380)

                    lbl_B = Label(font=["Arial", 14], fg="white", bg="black", text=cor2)
                    lbl_B.place(anchor=CENTER,  x=340,y=80)

                    cor3 = 180-cor2-cor1
                    lbl_C = Label(font=["Arial", 14], fg="white", bg="black", text=cor3)
                    lbl_C.place(anchor=CENTER,  x=480,y=380)

                    lbl_teor = Label(justify=LEFT, font=["Arial", 22],bg="black", fg="White", text=f"∠C = 180 - (∠A+∠B) \n∠C = 180 - ({cor1} + {cor2})\n∠C = 180 - {cor1+cor2}\n∠C = {cor3}")
                    lbl_teor.place( anchor=CENTER,x=700, y=200)
                
        error_str = StringVar()
        lbl_error = Label(textvariable=error_str, font=["Arial", 14], fg="red", bg="black")
        lbl_error.place(anchor=CENTER, x=285, y=520)

        if corner == 'A':
            entry_B = Entry(width=5, validate='key', validatecommand=vcmd)
            entry_B.place(anchor=CENTER, x=330,y=80)

            entry_C = Entry(width=5, validate='key', validatecommand=vcmd)
            entry_C.place(anchor=CENTER, x=470,y=380)

            btn_start = Button(text="Найти угол",font=["Arial",14], width=15, height=2, command=lambda: start(entry_B, entry_C))
            btn_start.place(anchor=CENTER, x=285, y=470)

        elif corner == 'B':
            entry_A = Entry(width=5, validate='key', validatecommand=vcmd)
            entry_A.place(anchor=CENTER, x=200,y=380)

            entry_C = Entry(width=5, validate='key', validatecommand=vcmd)
            entry_C.place(anchor=CENTER, x=470,y=380)

            btn_start = Button(text="Найти угол",font=["Arial",14], width=15, height=2, command=lambda: start(entry_A, entry_C))
            btn_start.place(anchor=CENTER, x=285, y=470)

        elif corner == 'C':
            entry_A = Entry(width=5, validate='key', validatecommand=vcmd)
            entry_A.place(anchor=CENTER, x=200,y=380)

            entry_B = Entry(width=5, validate='key', validatecommand=vcmd)
            entry_B.place(anchor=CENTER, x=330,y=80)

            btn_start = Button(text="Найти угол",font=["Arial",14], width=15, height=2, command=lambda: start(entry_A, entry_B))
            btn_start.place(anchor=CENTER, x=285, y=470)



    lbl_info = Label(font=["Arial",14], bg="black", fg="White", text="Выберите угол который необходимо найти")
    lbl_info.place(anchor=CENTER, x=300, y=40)

    lbl_B = Label(font=["Arial",14], bg="black", fg="White", text="B")
    lbl_B.place(anchor=CENTER, x=300,y=80)

    lbl_A = Label(font=["Arial",14], bg="black", fg="White", text="A")
    lbl_A.place(anchor=CENTER, x=150,y=380)

    lbl_C = Label(font=["Arial",14], bg="black", fg="White", text="C")
    lbl_C.place(anchor=CENTER, x=440,y=380)

    btn_B = Button(width=5, height=2, text="B", command=lambda: search('B'))
    btn_B.place(anchor=CENTER, x=300,y=80)

    btn_C = Button(width=5, height=2, text="C", command=lambda: search('C'))
    btn_C.place(anchor=CENTER,  x=440,y=380)

    btn_A = Button(width=5, height=2, text="A", command=lambda: search('A'))
    btn_A.place(anchor=CENTER, x=150,y=380) 

    btn_back= Button(text="В меню", width=8, height=2, compound="top",  font=("Arial", 16), command=lambda: MainWin.MainWin(main_win))
    btn_back.place(anchor="c", y=50, x = 1000)