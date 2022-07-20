from tkinter import *

def open() :
    logiciel.run()

window_exe = Tk()
window_exe.geometry("500x400")
window_exe.title("Lancement de Gest'Watch Secure")
window_exe.config(bg="#FFE4C4")

frame_exe = Frame(window_exe, bg="#FFE4C4")
frame_exe.grid(row=0, column=0)

lb = Label(frame_exe, text="Lancement du programme de protection du logiciel Gest'Watch", font=("Times New Roman", 14), bg="#FFE4C4", fg="black")
lb.grid(row=0, column=0)

bt = Button(frame_exe, text="Executer", font=("Times New Roman", 12), bg="#87CEFA", fg="black", width=10, height=1, command=open)
bt.grid(row=1, column=0)

window_exe.mainloop()