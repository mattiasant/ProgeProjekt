import tkinter as tk
from tkinter import ttk
import pygame

'''
def show_selected():
    selected_reso = reso_combo.get()
    fscreen = var1.get()
    sound = var2.get()

    print(f"Valitud resolutsioon: {selected_reso}")
    print(f"Valitud täisekraan: {fscreen}")
    print(f'Sound is {sound}')
'''

root = tk.Tk()
root.title("Setup")
root.geometry("400x350")
root.iconbitmap("icon.ico")
setupdone = False


def sule():
    global setupdone
    global suurus
    global scale
    global heli
    scale = sisend.get()
    setupdone = True
    suurus = reso_combo.get()
    heliväärtus = checkbox

    root.destroy()

    return True


def vahe():
    label = tk.Label(root, text='')
    label.pack(padx=20, pady=10)


# Dropdown for language selection
pygame.init()
reso = tk.Label(root, text="Resolution", padx=20, pady=5)
reso.pack()
valikud = pygame.display.list_modes()
reso_combo = ttk.Combobox(root, values=valikud)
reso_combo.pack()

vahe()
label = tk.Label(root, text='Scaling %')
label.pack()
sisend = tk.Entry(root)
sisend.pack()

vahe()

var1 = tk.IntVar()
checkbox = tk.Checkbutton(root, text='Fullscreen', variable=var1)
checkbox.pack()

vahe()

var2 = tk.IntVar(value=1)
checkbox = tk.Checkbutton(root, text='Sound', variable=var2)
checkbox.pack()

vahe()

show_button = tk.Button(root, text="Start", command=sule)
show_button.pack()

root.mainloop()
