from tkinter import *
import time
from datetime import date
import importlib

LIGHT = "#FFF0F5"
PEACH = '#FBA1B7'
PURPULE = "#916DB3"
FONT_NAME = "Courier"

master = Tk()
master.minsize(width=700, height=500)
master.config(padx=10, pady=10, bg=LIGHT)
master.title('TimeLife by Celina')
canvas = Canvas(width=10, height=10)

timenow = ' '
cframe = Frame(master, width = 50, height=20, bg=LIGHT, relief=RAISED)
cframe.grid(row=0,column=0)

clock = Label(cframe, padx=25, pady=40, bd=3,
              font=(FONT_NAME, 45, "bold"), text=timenow, relief=RAISED)
clock.grid(row=0,column=0)

img = PhotoImage(file="obrazek.png")
background_label = Label(master, image=img)
background_label.grid(row=0,column=1)

def tick():
    global timenow
    newtime = time.strftime('%H: %M: %S %p')
    if newtime != timenow:
        timenow = newtime
        clock.config(text=timenow, fg=PURPULE, bg=LIGHT, font=(FONT_NAME, 45, "bold"))

    return clock.after(100,tick)

def submit():

    dateOfBirth = date(int(year.get()), int(month.get()), int(day.get()))
    delta = date.today() - dateOfBirth
    napis = Label(text=f'Dzisiaj jest: {date.today()} '
                       f'\nPrzeżyłeś już {delta}, {timenow}', fg=PURPULE,
                  bg=PEACH)
    napis.grid(row=7, column=0)

def close():
    master.destroy()


year = Entry(width=35)
year.insert(END, string="Jaki jest twój rok urodzenia? RRRR")
year.grid(column=0, pady=2, sticky=W)

month = Entry(width=35)
month.insert(END, string="Jaki jest twój miesiąc urodzenia? MM")
month.grid(column=0, pady=2, sticky=W)

day = Entry(width=35)
day.insert(END, string="Jaki jest twój dzień urodzenia? DD")
day.grid(column=0, pady=2, sticky=W)

b1 = Button(text="How many days did you live?", command=submit, width=32,
            fg=PURPULE, bg=LIGHT, font=(FONT_NAME, 10, "bold"))
b1.grid(row=1, column=0, sticky=E)

close = Button(text="close", command=close, fg=PURPULE, bg=LIGHT, font=(FONT_NAME, 10, "bold"))
close.grid(row=2, column=1, sticky=E)

tick()
master.mainloop()