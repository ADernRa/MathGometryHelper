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
        per = float(ent_per.get())
        val = float(ent_val.get())
        clear.ClearWin(main_win)

        btn_back= Button(text="В начало", width=8, height=2, compound="top",  font=("Arial", 16), command=lambda: search_percent(main_win))
        btn_back.place(anchor="c", y=130, x = 1000)
        
        btn_menu= Button(text="В меню", width=8, height=2, compound="top",  font=("Arial", 16), command=lambda: MainWin.MainWin(main_win))
        btn_menu.place(anchor="c", y=50, x = 1000)

        lbl_val = Label(font=("Arial", 15),text=f"x = {val}", bg="black", fg="white")
        lbl_val.place(anchor=CENTER, x = 120, y = 100)

        lbl_per = Label(font=("Arial", 15),text=f"y = {per}%", bg="black", fg="white")
        lbl_per.place(anchor=CENTER, x = 270, y = 100)

        lbl_info_new = Label(font=("Arial", 15),text="Введите значение", bg="black", fg="white")
        lbl_info_new.place(anchor=CENTER, x = 200, y = 150)
        
        def start():
            if action == "value":
                if ent_per_search.get() == '':
                    error_str.set("Необходимо ввести значение")
                    return
                elif float(ent_per_search.get()) == 0:
                    error_str.set("Значения должны быть > 0")
                    return
                
                per_search = float(ent_per_search.get())
                btn_start.destroy()
                ent_per_search.destroy()

                lbl_per_search_ = Label(font=("Arial", 15),text=f"y0 = {per_search}%", bg="black", fg="white")
                lbl_per_search_.place(anchor=CENTER, x = 270, y = 200)

                val_search = val*per_search/per
                lbl_val_search["text"] = f"x0 = {val_search}"

                lbl_teor = Label(justify=LEFT, font=["Arial", 22],bg="black", fg="White", text=f"x0 = (x*y0)/y\nx0 = ({val}*{per_search})/{per}\nx0 = {val*per_search/per}")
                lbl_teor.place( anchor=CENTER,x=700, y=200)
            
            if action == "percent":
                if ent_val_search.get() == '':
                    error_str.set("Необходимо ввести значение")
                    return
                elif float(ent_val_search.get()) == 0:
                    error_str.set("Значения должны быть > 0")
                    return
                
                val_search = float(ent_val_search.get())
                btn_start.destroy()
                ent_val_search.destroy()

                lbl_val_search_ = Label(font=("Arial", 15),text=f"x0 = {val_search}", bg="black", fg="white")
                lbl_val_search_.place(anchor=CENTER, x = 120, y = 200)

                per_search = per*val_search/val
                lbl_per_search["text"] = f"y0 = {per_search}%"

                lbl_teor = Label(justify=LEFT, font=["Arial", 22],bg="black", fg="White", text=f"y0 = (y*x0)/x\ny0 = ({per}*{val_search})/{val}\ny0 = {per*val_search/val}")
                lbl_teor.place( anchor=CENTER,x=700, y=200)
            
            lbl_info_new.destroy()

        if action == "value":
            ent_per_search = Entry(font=("Arial", 15), justify=RIGHT, width=12, validate='key', validatecommand=vcmd,bg="gray", fg="black")
            ent_per_search.place(anchor=CENTER, x = 270, y = 200)

            lbl_val_search = Label(font=("Arial", 15),text=f"???", bg="black", fg="white")
            lbl_val_search.place(anchor=CENTER, x = 120, y = 200)

            btn_start = Button(text="Начать поиск",font=["Arial",13], width=15, height=2, command=start)
            btn_start.place(anchor=CENTER, x = 195, y = 250)

        if action == "percent":
            lbl_per_search = Label(font=("Arial", 15),text=f"???", bg="black", fg="white")
            lbl_per_search.place(anchor=CENTER, x = 270, y = 200)

            ent_val_search = Entry(font=("Arial", 15), justify=RIGHT, width=12, validate='key', validatecommand=vcmd,bg="gray", fg="black")
            ent_val_search.place(anchor=CENTER, x = 120, y = 200)

            btn_start = Button(text="Начать поиск",font=["Arial",13], width=15, height=2, command=start)
            btn_start.place(anchor=CENTER, x = 195, y = 250)

    
    ent_val = Entry(font=("Arial", 15), justify=RIGHT, width=12,validate='key', validatecommand=vcmd,bg="gray", fg="black")
    ent_val.place(anchor=CENTER, x = 120, y = 100)

    ent_per = Entry(font=("Arial", 15), justify=RIGHT, width=12, validate='key', validatecommand=vcmd,bg="gray", fg="black")
    ent_per.place(anchor=CENTER, x = 270, y = 100)

    lbl_info = Label(font=("Arial", 15),text="Выберите что хотите найти", bg="black", fg="white")
    lbl_info.place(anchor=CENTER, x = 200, y = 150)

    btn_val = Button(text="Число",font=["Arial",13], width=15, height=2, command=lambda: search("value"))
    btn_val.place(anchor=CENTER, x = 120, y = 200)

    btn_per = Button(text="Процент",font=["Arial",13], width=15, height=2, command=lambda: search("percent"))
    btn_per.place(anchor=CENTER, x = 270, y = 200)

    lbl_syb_per = Label(font=("Arial", 15),text="%", bg="black", fg="white")
    lbl_syb_per.place(anchor=CENTER, x = 350, y = 100)

    lbl_val = Label(font=("Arial", 15),text="Число", bg="black", fg="white")
    lbl_val.place(anchor=CENTER, x = 120, y = 65)

    lbl_per = Label(font=("Arial", 15),text="Процент", bg="black", fg="white")
    lbl_per.place(anchor=CENTER, x = 270, y = 65)

    btn_menu= Button(text="В меню", width=8, height=2, compound="top",  font=("Arial", 16), command=lambda: MainWin.MainWin(main_win))
    btn_menu.place(anchor="c", y=50, x = 1000)