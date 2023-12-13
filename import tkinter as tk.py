import tkinter as tk
from time import strftime
def update_time() :
    time = strftime('%H:%M:%S %p')
    lbl.config(text = time)
    lbl.after(1000, update_time)


root = tk.Tk()

root.title("Digital clock")

lbl = tk.Label(root, font = ('keep on truckin', 50,), background = 'black', foreground = 'white')
lbl.pack(anchor = 'center')
update_time()
root.mainloop()