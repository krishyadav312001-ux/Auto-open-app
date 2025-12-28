import pyautogui as gui
import subprocess
import time

def open_App(text):
    text = text.lower().strip()

    apps = {
        "chrome": "chrome.exe",
        "notepad": "notepad.exe",
        "vscode": "code.exe",
        "visual studio code": "code.exe",
        "word": "winword.exe",
        "excel": "excel.exe",
        "powerpoint": "powerpnt.exe",
        "paint": "mspaint.exe",
        "cmd": "cmd.exe",
        "calculator": "calc.exe",
        "file explorer": "explorer.exe",
        "edge": "msedge.exe"
    }

    try:
        if text in apps:
            subprocess.Popen(apps[text])
        else:
            raise Exception("App not found")
    except:
        # Fallback: Windows search
        gui.press("win")
        time.sleep(0.3)
        gui.write(text)
        time.sleep(1)
        gui.press("enter")


while True:
    x = input("x : ")
    open_App(x)
