import tkinter as tk
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
root.geometry("400x240")
root.iconbitmap("icon.ico")
setupdone = False


def sule():
    global setupdone
    global suurus
    global scale
    global heli
    setupdone = True
    heliväärtus = checkbox

    root.destroy()

    return True


def vahe():
    label = tk.Label(root, text='')
    label.pack(padx=20, pady=10)


# Dropdown for language selection
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
