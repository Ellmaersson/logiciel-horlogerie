from tkinter import *
import urllib.request
from tkinter import ttk


def action_cbbox() :

    # Obtenir l'élément sélectionné
    select = listeCombo.get()
    print("La mise à jour est prête pour initialisation et pour téléchargement !'", select, "'")
    urllib.request.urlretrieve(select, "", Telecharger.reporthook)

def parametre() :
    parametre_window = Tk()
    parametre_window.geometry("700x500")
    parametre_window.iconbitmap("roue_d12-_3_.ico")
    parametre_window.title("Paramètre du logiciel")
    parametre_window.config(bg="white")

    Framemise_a_jour = Frame(parametre_window, bg="white", width=20, height=1)
    Framemise_a_jour.grid(row=0, column=0)

    Label(Framemise_a_jour, text="A propos :",font=("Times New Roman", 16), bg="white", fg="black",width=10).grid(row=0, column=0)

    space = Label(Framemise_a_jour, text="", bg="white", width=10, height=1)
    space.grid(row=2, column=0)

    Label(Framemise_a_jour, text="Le téléchargement de la mise à jour est disponible !", font=("Times NEw Roman", 12), bg="white", fg="red", width=40).grid(row=2, column=0)

    version_label = Label(Framemise_a_jour, text="Version de la mise à jour à télécharger :", font=("Times New Roman", 12), bg="white", fg="black", width=40, height=1)
    version_label.grid(row=3, column=0)

    liste_maj = ["v 1.0.01", "v1.0.02"]

    listeCombo = ttk.Combobox(Framemise_a_jour, values=liste_maj)
    listeCombo.current(0)
    listeCombo.grid(row=3, column=1)
    listeCombo.bind("<<listeCombo>>", action_cbbox)

    space = Label(Framemise_a_jour, text="", bg="white", width=10, height=1)
    space.grid(row=4, column=0)

    telechargement_bouton = Button(Framemise_a_jour, text="Téléchargement", font=("Times New Roman", 14), bg="lime", width=15, height=1, command=action_cbbox)
    telechargement_bouton.grid(row=4, column=1)


window = Tk()

window.title("Λκδμ Gest'Watch")
window.geometry("1530x900")
window.iconbitmap("Lambda-logo.ico")
window.config(bg="white")

acceuil_frame = Frame(window, bg="white", width=20, height=1)
acceuil_frame.grid(row=0, column=0)

label_titre = Label(acceuil_frame, text="Logiciel d'horlogerie Gest'Watch", font=("Times New Roman", 16), bg="white", fg="black", width=30, height=1)
label_titre.grid(row=0, column=0)

aide_bouton = Button(acceuil_frame, text="Paramètre", font=("Times New Roman", 14), bg="#87CEFA", fg="black", width=10, height=1,command=parametre)
aide_bouton.grid(row=1, column=0)


window.mainloop()
