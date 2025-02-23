def ClearWin(main_win):
    for widget in main_win.winfo_children():
        widget.destroy()