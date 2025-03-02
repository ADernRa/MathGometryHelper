from tkinter import *
import clear
import MainWin
import math

def corners_table(main_win):
    clear.ClearWin(main_win)

    def validate(new_value):
        my_list = ['1','2','3','4','5','6','7','8','9','0']
        return all(c in my_list for c in new_value)
    
    vcmd = (main_win.register(validate), '%P')

    global page
    page = 1
    values = 15

    lbl_one = Label(text="",justify=LEFT, bg="black", fg="white", font=["Arial", 14])
    lbl_one.place(anchor=NW,  x=80, y=40)

    lbl_two = Label(text="",justify=LEFT, bg="black", fg="white", font=["Arial", 14])
    lbl_two.place(anchor=NW,  x=325, y=40)
    
    lbl_three = Label(text="",justify=LEFT, bg="black", fg="white", font=["Arial", 14])
    lbl_three.place(anchor=NW,  x=550, y=40)
    
    lbl_four = Label(text="",justify=LEFT, bg="black", fg="white", font=["Arial", 14])
    lbl_four.place(anchor=NW,  x=800, y=40)

    def page_list(action: str, value_ent: Entry = 1):
        global page
        my_page = ["","","",""]
        if(action == "start"):
            for val in range((page-1)*values , page*values+1):
                my_page[0] = my_page[0] + f"sin({val}) = {round(math.sin(val),2)}\n"
                my_page[1] = my_page[1] + f"cos({val}) = {round(math.cos(val),2)}\n"
                my_page[2] = my_page[2] + f"tan({val}) = {round(math.tan(val),2)}\n"
                if math.sin(val) == 0:
                    my_page[3] = my_page[3] + f"ctg({val}) = - \n"
                else:
                    my_page[3] = my_page[3] + f"ctg({val}) = {round(math.cos(val)/math.sin(val), 2)}\n"
                

        elif(action == "right"):
            page = page + 1
            for val in range((page-1)*values , page*values+1):
                val = val +1
                my_page[0] = my_page[0] + f"sin({val}) = {round(math.sin(val),2)}\n"
                my_page[1] = my_page[1] + f"cos({val}) = {round(math.cos(val),2)}\n"
                my_page[2] = my_page[2] + f"tan({val}) = {round(math.tan(val),2)}\n"
                if math.sin(val) == 0:
                    my_page[3] = my_page[3] + f"ctg({val}) = - \n"
                else:
                    my_page[3] = my_page[3] + f"ctg({val}) = {round(math.cos(val)/math.sin(val), 2)}\n"


        elif(action == "left"):
            if(page==1):
                return
            
            page = page - 1
            for val in range((page-1)*values , page*values+1):
                if page != 1:
                    val = val + 1
                my_page[0] = my_page[0] + f"sin({val}) = {round(math.sin(val),2)}\n"
                my_page[1] = my_page[1] + f"cos({val}) = {round(math.cos(val),2)}\n"
                my_page[2] = my_page[2] + f"tan({val}) = {round(math.tan(val),2)}\n"
                if math.sin(val) == 0:
                    my_page[3] = my_page[3] + f"ctg({val}) = - \n"
                else:
                    my_page[3] = my_page[3] + f"ctg({val}) = {round(math.cos(val)/math.sin(val), 2)}\n"


        elif(action == "search"):
            value = int(value_ent.get())
            if(value<1):
                error_str.set("Значение должно быть > 0")
                return
            elif(value>1000):
                error_str.set("Значение должно быть < 1001")
                return
        
            while True:
                if (page-1)*values < value and values+(page-1)*values < value:
                    page = page + 1
                elif (page-1)*values > value and values+(page-1)*values > value:
                    page = page - 1
                else:
                    break
                    
            for val in range((page-1)*values , page*values+1):
                if page != 1:
                    val = val + 1
                my_page[0] = my_page[0] + f"sin({val}) = {round(math.sin(val),2)}\n"
                my_page[1] = my_page[1] + f"cos({val}) = {round(math.cos(val),2)}\n"
                my_page[2] = my_page[2] + f"tan({val}) = {round(math.tan(val),2)}\n"
                if math.sin(val) == 0:
                    my_page[3] = my_page[3] + f"ctg({val}) = - \n"
                else:
                    my_page[3] = my_page[3] + f"ctg({val}) = {round(math.cos(val)/math.sin(val), 2)}\n"


        lbl_one["text"] = my_page[0]
        lbl_two["text"] = my_page[1]
        lbl_three["text"] = my_page[2]
        lbl_four["text"] = my_page[3]


    page_list("start")

    ent_num = Entry(width=15, validate='key', validatecommand=vcmd)
    ent_num.place(anchor=CENTER, x=540, y=450)

    btn_search = Button(text="Начать поиск", width=12, height=1, compound="top",  font=("Arial", 16), command=lambda: page_list("search", ent_num))
    btn_search.place(anchor=CENTER, x=540, y=500)

    btn_left = Button(text="<", width=2, height=1, compound="top",  font=("Arial", 16), command=lambda: page_list("left"))
    btn_left.place(anchor=CENTER, x=400, y=500)

    btn_right = Button(text=">", width=2, height=1, compound="top",  font=("Arial", 16), command=lambda: page_list("right"))
    btn_right.place(anchor=CENTER, x=680, y=500)

    error_str = StringVar()
    lbl_error = Label(textvariable=error_str, font=["Arial", 14], fg="red", bg="black")
    lbl_error.place(anchor=CENTER, x=540, y=400)

    btn_back= Button(text="В меню", width=8, height=2, compound="top",  font=("Arial", 16), command=lambda: MainWin.MainWin(main_win))
    btn_back.place(anchor="c", y=500, x = 1000)