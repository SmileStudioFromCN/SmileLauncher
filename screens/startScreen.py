# copyright (c) 2024 Smile Studio

import tkinter as tk
import lang

lang = lang.lang()

def laguageChange():
    print("language")

def run():
    root = tk.Tk()
    root.title(lang["welcome_title"])
    root.geometry("400x400")


    welcome_label = tk.Label(root, text="Welcome to Smile Launcher", font=("Arial", 16))
    welcome_label.pack(pady=20)
    language_label = tk.Label(root, text="please select your language", font=("Arial", 12))
    language_label.pack()

    root.mainloop()