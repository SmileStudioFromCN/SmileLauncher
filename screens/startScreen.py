# copyright (c) 2024 Smile Studio

import tkinter as tk
import ml
import lang

lang = lang.lang()

def laguageChange():
    print("language")

def run():
    root = tk.Tk()
    root.title(lang["welcome_title"])
    root.geometry("500x300")


    welcome_label = tk.Label(root, text=lang["welcome_title"], font=("Arial", 16))
    welcome_label.pack(pady=20)
    subtitle_label = tk.Label(root, text=lang["welcome_subtitle"], font=("Arial", 12))
    subtitle_label.pack()

    root.mainloop()