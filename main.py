import tkinter as tk

window = tk.Tk()
window.configure()
window.title("PLQA Multi-Tool by gvan")


def handle_button_press():
    window.destroy()


button = tk.Button(text="die", command=handle_button_press)
button.pack()

window.mainloop()
##apple
##newCommi