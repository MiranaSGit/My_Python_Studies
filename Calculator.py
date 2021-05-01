from tkinter import Canvas, messagebox, Tk, Button, Menu, Label, Scale, SUNKEN, HORIZONTAL, RAISED, VERTICAL, Entry, Text, LEFT
window_main=Tk()
window_main.resizable(0, 0)
screen_width = 400
screen_height = 600
screen_resolution = (screen_width, screen_height)   # Golden Ratio
main_window_dimensions = str(screen_resolution[0])+'x'+str(screen_resolution[1])
window_main.geometry(main_window_dimensions)
window_main.title("Simple Demo App. with tkinter")
def getnumber1():
    temp_pos = len(user_entry.get())
    user_entry.insert(temp_pos, "1")
def getnumber2():
    temp_pos = len(user_entry.get())
    user_entry.insert(temp_pos, "2")
label_header = Label(window_main, text="A Simple Calculator", font=("arial", 24), relief=SUNKEN, width=20)
label_header.grid(row=0, columnspan=20)
user_entry = Entry(window_main, fg="white", bg="black", insertbackground='white', font=("arial", 24), width=20)
user_entry.grid(row=1, columnspan=20)
user_entry.focus_set()
button_1 = Button(window_main, text="1", font=("arial", 14, "bold"), command = getnumber1)
button_1.grid(row=2, column=0)
button_2 = Button(window_main, text="2", font=("arial", 14, "bold"), command = getnumber2)
button_2.grid(row=2, column=1)
button_3 = Button(window_main, text="3", font=("arial", 14, "bold"))
button_3.grid(row=2, column=2)
button_4 = Button(window_main, text="4", font=("arial", 14, "bold"))
button_4.grid(row=2, column=3)
button_5 = Button(window_main, text="5", font=("arial", 14, "bold"))
button_5.grid(row=2, column=4)
button_6 = Button(window_main, text="6", font=("arial", 14, "bold"))
button_6.grid(row=3, column=0)
button_7 = Button(window_main, text="7", font=("arial", 14, "bold"))
button_7.grid(row=3, column=1)
button_8 = Button(window_main, text="8", font=("arial", 14, "bold"))
button_8.grid(row=3, column=2)
button_9 = Button(window_main, text="9", font=("arial", 14, "bold"))
button_9.grid(row=3, column=3)
button_0 = Button(window_main, text="0", font=("arial", 14, "bold"))
button_0.grid(row=3, column=4)
button_plus = Button(window_main, text="+", font=("arial", 14, "bold"))
button_plus.grid(row=4, column=0)
button_minus = Button(window_main, text="-", font=("arial", 14, "bold"))
button_minus.grid(row=4, column=1)
button_div = Button(window_main, text="/", font=("arial", 14, "bold"))
button_div.grid(row=4, column=2)
button_mult = Button(window_main, text="*", font=("arial", 14, "bold"))
button_mult.grid(row=4, column=3)
button_sqr = Button(window_main, text="**", font=("arial", 14, "bold"))
button_sqr.grid(row=4, column=4)
window_main.mainloop()