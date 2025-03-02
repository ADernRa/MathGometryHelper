from tkinter import *
import clear
import MainWin

def calculator(main_win):
    
    clear.ClearWin(main_win)

    def add(symbol):
        lbl_text.insert(len(lbl_text.get()), symbol)    
    
    def clear_all():
        lbl_text.delete(0, END)

    def clear_last():
        lbl_text.delete(len(lbl_text.get()) - 1, END)

    def validate(new_value):
        my_list = ['1','2','3','4','5','6','7','8','9','0','/','*','-','+','.','(',')']
        return all(c in my_list for c in new_value)

    def result():
        try:
            res = eval(lbl_text.get())
            lbl_text.delete(0, END)
            lbl_text.insert(0, res)
            error_str.set(" ")
        except ZeroDivisionError:
            error_str.set("Невозможно поделить на 0")
        except:
            error_str.set("Невозможно посчитать")

    canvas = Canvas(bg="white", highlightbackground = "white", width=290, height=340)
    canvas.place(anchor=CENTER,  y=330, x = 557)
    canvas.create_rectangle(5, 10, 289, 115, fill="gray", outline="gray")

    error_str = StringVar()
    lbl_error = Label(textvariable=error_str, font=["Arial", 30], fg="red", bg="black")
    lbl_error.place(anchor=CENTER, x=557, y=100)
    
    vcmd = (main_win.register(validate), '%P')
    lbl_text = Entry(text="0",bg="gray", fg="black",font=("Arial", 30), justify=RIGHT, width=12, validate='key', validatecommand=vcmd)
    lbl_text.place(anchor="c", y=200, x = 560)

    btn_one= Button(text="1", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add(1))
    btn_one.place(anchor="c", y=270, x = 500)

    btn_two= Button(text="2", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add(2))
    btn_two.place(anchor="c", y=270, x = 557)

    btn_three= Button(text="3", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add(3))
    btn_three.place(anchor="c", y=270, x = 614)

    btn_plus= Button(text="+", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add('+'))
    btn_plus.place(anchor="c", y=270, x = 671)

    btn_four= Button(text="4", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add(4))
    btn_four.place(anchor="c", y=336, x = 500)

    btn_five = Button(text="5", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add(5))
    btn_five.place(anchor="c", y=336, x = 557)

    btn_six = Button(text="6", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add(6))
    btn_six.place(anchor="c", y=336, x = 614)

    btn_minus= Button(text="-", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add('-'))
    btn_minus.place(anchor="c", y=336, x = 671)

    btn_seven = Button(text="7", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add(7))
    btn_seven.place(anchor="c", y=402, x = 500)

    btn_eight = Button(text="8", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add(8))
    btn_eight.place(anchor="c", y=402, x = 557)

    btn_nine = Button(text="9", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add(9))
    btn_nine.place(anchor="c", y=402, x = 614)

    btn_multiply= Button(text="*", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add('*'))
    btn_multiply.place(anchor="c", y=402, x = 671)

    btn_seven = Button(text="0", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add(0))
    btn_seven.place(anchor="c", y=467, x = 500)

    btn_dot = Button(text=".", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add('.'))
    btn_dot.place(anchor="c", y=467, x = 557)

    btn_equals = Button(text="=", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=result)
    btn_equals.place(anchor="c", y=467, x = 614)
    
    btn_divide= Button(text="/", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add('/'))
    btn_divide.place(anchor="c", y=467, x = 671)

    btn_left_bracket= Button(text="(", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add('('))
    btn_left_bracket.place(anchor="c", y=270, x = 443)

    btn_right_bracket= Button(text=")", width=4, height=2, compound=CENTER,  font=("Arial", 16), command=lambda: add(')'))
    btn_right_bracket.place(anchor="c", y=336, x = 443)

    btn_del = Button(text="⌫", width=4, height=2, compound=CENTER,  font=("Arial", 16), command= clear_last)
    btn_del.place(anchor="c", y=402, x = 443)

    btn_del_all = Button(text="🗑️", width=4, height=2, compound=CENTER,  font=("Arial", 16), command= clear_all)
    btn_del_all.place(anchor="c", y=467, x = 443)

    btn_back= Button(text="В меню", width=8, height=2, compound="top",  font=("Arial", 16), command=lambda: MainWin.MainWin(main_win))
    btn_back.place(anchor="c", y=200, x = 300)
    lbl_text.focus()