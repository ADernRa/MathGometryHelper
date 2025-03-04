from tkinter import *
import clear
import MainWin

def search_percent(main_win):
    clear.ClearWin(main_win)

    def validate(new_value):
        my_list = ['1','2','3','4','5','6','7','8','9','0','.']
        return all(c in my_list for c in new_value)
    
    vcmd = (main_win.register(validate), '%P')

    error_str = StringVar()
    lbl_error = Label(textvariable=error_str, font=["Arial", 14], fg="red", bg="black")
    lbl_error.place(anchor=CENTER, x=285, y=520)

    def search(action: str):
        if ent_val.get() == '' or ent_per.get() == '':
                error_str.set("Необходимо ввести значение")
                return
        elif float(ent_val.get()) == 0 or float(ent_per.get()) == 0:
            error_str.set("Значения должны быть > 0")
            return
        
        error_str.set("")
        per = ent_per.get()
        val = ent_val.get()
        clear.ClearWin(main_win)

        lbl_val = Label(font=("Arial", 15),text=f"{val}", bg="black", fg="white")
        lbl_val.place(anchor=CENTER, x = 120, y = 100)

        lbl_per = Label(font=("Arial", 15),text=f"{per}%", bg="black", fg="white")
        lbl_per.place(anchor=CENTER, x = 270, y = 100)

        lbl_info_new = Label(font=("Arial", 15),text="Вв", bg="black", fg="white")
        lbl_info_new.place(anchor=CENTER, x = 200, y = 150)

    
    ent_val = Entry(font=("Arial", 15), justify=RIGHT, width=12,validate='key', validatecommand=vcmd,bg="gray", fg="black")
    ent_val.place(anchor=CENTER, x = 120, y = 100)

    ent_per = Entry(font=("Arial", 15), justify=RIGHT, width=12, validate='key', validatecommand=vcmd,bg="gray", fg="black")
    ent_per.place(anchor=CENTER, x = 270, y = 100)

    lbl_info = Label(font=("Arial", 15),text="Выберите что хотите найти", bg="black", fg="white")
    lbl_info.place(anchor=CENTER, x = 200, y = 150)

    btn_val = Button(text="Число",font=["Arial",13], width=15, height=2, command=lambda: search("qwe"))
    btn_val.place(anchor=CENTER, x = 120, y = 200)

    btn_per = Button(text="Процент",font=["Arial",13], width=15, height=2, command=lambda: search("qwe"))
    btn_per.place(anchor=CENTER, x = 270, y = 200)

    lbl_syb_per = Label(font=("Arial", 15),text="%", bg="black", fg="white")
    lbl_syb_per.place(anchor=CENTER, x = 350, y = 100)

    lbl_val = Label(font=("Arial", 15),text="Число", bg="black", fg="white")
    lbl_val.place(anchor=CENTER, x = 120, y = 65)

    lbl_per = Label(font=("Arial", 15),text="Процент", bg="black", fg="white")
    lbl_per.place(anchor=CENTER, x = 270, y = 65)