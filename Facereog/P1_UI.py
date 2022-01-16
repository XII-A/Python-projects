import tkinter as tk
from tkinter.constants import W
from P1_F import *
import time
import keyboard
import threading
import sys 
import os

window = tk.Tk()
def killing():
    #window.destroy()
    sys.exit()
    
def main():
    global window

    window.title("Brighten Screen")
    
    Starter = tk.Button(window, text='Click to start the program', padx=40, pady=20, command=threading.Thread(target=command_A).start()).grid(row=0, column=0)

    Ender = tk.Button(window,text='Click to end the program', padx=40, pady=20, command=threading.Thread(target=killing).start()).grid(row=0, column=1)

    window.mainloop()



if __name__ == '__main__':
    main()
    
    

    
