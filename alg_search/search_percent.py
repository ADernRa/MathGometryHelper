from tkinter import *
import clear
import MainWin

def search_percent(main_win):
    clear.ClearWin(main_win)

    def validate(new_value):
        my_list = ['1','2','3','4','5','6','7','8','9','0','.']
        return all(c in my_list for c in new_value)
    
    vcmd = (main_win.register(validate), '%P')
    
    ent_val = Entry(font=("Arial", 15), justify=RIGHT, width=12,validate='key', validatecommand=vcmd,bg="gray", fg="black")
    ent_val.place(anchor=CENTER, x = 120, y = 100)

    ent_per = Entry(font=("Arial", 15), justify=RIGHT, width=12, validate='key', validatecommand=vcmd,bg="gray", fg="black")
    ent_per.place(anchor=CENTER, x = 270, y = 100)

    lbl_syb_per = Label(font=("Arial", 15),text="%", bg="black", fg="white")
    lbl_syb_per.place(anchor=CENTER, x = 350, y = 100)

    lbl_val = Label(font=("Arial", 15),text="Число", bg="black", fg="white")
    lbl_val.place(anchor=CENTER, x = 120, y = 65)

    lbl_per = Label(font=("Arial", 15),text="Процент", bg="black", fg="white")
    lbl_per.place(anchor=CENTER, x = 270, y = 65)