from tkinter import *
from MainWin import MainWin
main_win = Tk()
    
def CreateWin():
    main_win.title("MathHelper")
    main_win.geometry("1080x540")
    main_win.resizable(False, False)
    main_win.config(bg="black")
    icon = PhotoImage(file = "icon.png")
    main_win.iconphoto(False, icon)


CreateWin()
MainWin(main_win)

main_win.mainloop()