# Tkinter-clock
This Python code uses the Tkinter library to create a simple digital clock GUI (Graphical User Interface). The digital clock displays the current time in hours, minutes, seconds, and AM/PM format. Here's a description of the code:

The `import tkinter as tk` statement imports the Tkinter module, which provides tools for creating GUI applications.

The `from time import strftime` statement imports the `strftime` function from the `time` module. This function is used to format the time.

The `update_time` function is defined to update the displayed time. It uses the `strftime` function to get the current time in the desired format ('%H:%M:%S %p'). The formatted time is then set as the text of the label (`lbl`). The `lbl.after(1000, update_time)` line schedules the `update_time` function to be called every 1000 milliseconds (1 second), creating a continuous update loop.

The `root = tk.Tk()` line initializes the main window of the Tkinter application.

The `root.title("Digital clock")` line sets the title of the main window to "Digital clock."

The `lbl = tk.Label(root, font=('keep on truckin', 50,), background='black', foreground='white')` line creates a label (`lbl`) to display the time. It sets the font, background color, and foreground color of the label.

The `lbl.pack(anchor='center')` line organizes the label within the main window and centers it.

The `update_time()` line initially calls the `update_time` function to display the current time.

Finally, `root.mainloop()` starts the main event loop of the Tkinter application, allowing the GUI to respond to user interactions and continuously update the displayed time.
