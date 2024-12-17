# copyright (c) 2024 Smile Studio

import tkinter as tk
import webbrowser
from requests import *
from json import *

back = ""

def set_back(url,window):
    global back
    back = url
    window.destroy()

def get_code():
    global back
    root = tk.Tk()
    root.title("微软登录")
    label = tk.Label(root, text="输入重定向后的链接")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    button = tk.Button(root, text="确认", command=lambda: set_back(entry.get(), root))
    button.pack()
    root.mainloop()

def ml(window):
    global back
    window.destroy()
    url = """https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize
        ?client_id=84806f65-8a4d-4b2c-a3d2-801081dfc2cd
         &response_type=code
         &redirect_uri=https://127.0.0.1:5000/get_code
         &response_mode=query
         &scope=XboxLive.signin offline_access"""
    webbrowser.open(url)

    get_code()
    code_full = back
    code = code_full.split("code=")[1]
    microsoft_token_dict = {"client_id": "84806f65-8a4d-4b2c-a3d2-801081dfc2cd",
    "code": code,
   "grant_type": "authorization_code",
    "redirect_uri": "https://127.0.0.1:5000/get_code",
    "scope": "XboxLive.signin offline_access"}
    print(microsoft_token_dict)
    microsoft_token_response = post("https://login.microsoftonline.com/consumers/oauth2/v2.0/token", json=dumps(microsoft_token_dict), headers={"Content-Type": "application/x-www-form-urlencoded"})
    microsoft_token_json = microsoft_token_response.json()
    print(microsoft_token_json)
    access_token = microsoft_token_json["access_token"]
    refresh_token = microsoft_token_json["refresh_token"]


def run():
    root = tk.Tk()
    root.title("欢迎使用Smile Launcher")
    root.geometry("500x300")


    welcome_label = tk.Label(root, text="欢迎使用Smile Launcher", font=("Arial", 16))
    welcome_label.pack(pady=20)
    subtitle_label = tk.Label(root, text="如需启动Minecraft，请通过微软验证。", font=("Arial", 12))
    subtitle_label.pack()
    verif_button = tk.Button(root, text="微软登录", command=lambda : ml(root))
    verif_button.pack(pady=20)

    root.mainloop()