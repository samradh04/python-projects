import pyautogui
import tkinter as tk 
from tkinter.filedialog import *

root = tk.Tk()

canvas1 = tk.Canvas(root,width = 300,height = 300)
canvas1.pack()

def takescreenshot():
    myScreenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myScreenshot.save(save_path+"_screenshot.png")

myButton = tk.Button(text="Take screenshot" , command = takescreenshot,font=10)
canvas1.create_window(150,150,window = myButton)

root.mainloop()