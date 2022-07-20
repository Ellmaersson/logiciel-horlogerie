from tkinter import *

window_astro = Tk()

window_astro.title("Astronomie")
window_astro.geometry("500x500")
window_astro.config("#ADD8E6")
window_astro.iconbitmap("Téléscope-James-Webb.ico")

frame_astro = Frame(window_astro, bg="#ADD8E6", width=20, height=1)
frame_astro.grid(row=0, column=0)



window_astro.mainloop()