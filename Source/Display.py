import os
import tkinter as tk
from tkinter import ttk
from keyboard_functions import *

# Display Here!
def display():
    '''FUNCTION DISPLAY'''
    Main_Window = tk.Tk()

    Main_Window.iconbitmap('D:/PythonProject/CleaningKeyboard/assets/icon2.ico')
    Main_Window.geometry('500x300')
    Main_Window.title('Cleaning Keyboard')
    Main_Window.configure(bg='white')
    Main_Window.resizable(False,False)

    atribut(Main_Window)

# Atribut Here!
def atribut(MW):
    '''FUNCTION ATRIBUT'''
    # Frame
    input_frame = ttk.Frame()
    # Label
    label = ttk.Label(input_frame, text="CLEAN YOUR KEYBOARD WITHOUT TRUN OFF YOUR LAPTOP")
    title = ttk.Label(input_frame, text="Disable Your Keyboard")
    subTitle = ttk.Label(input_frame, text="-Close the window to end process-")

    # Combobox
    # data_combobox = ['Disable', 'Undisable']
    # Combobox = ttk.Combobox(input_frame, values= data_combobox)

    # Button
    Seccond_Dummy_label = ttk.Label(input_frame, text="")
    button_blockkey = ttk.Button(input_frame, text= "Disable", command= functionBlockKey)
    button_unblockkey = ttk.Button(input_frame, text= "Enable", command= functionUnblockKey)

    # Pack
    input_frame.pack(padx=10,pady=10,fill='x',expand=True)
    label.pack()
    title.pack()
    subTitle.pack()
    # Combobox.pack()
    Seccond_Dummy_label.pack()
    button_blockkey.pack(pady= 5)
    button_unblockkey.pack(pady= 5)
    MW.mainloop()

'''
# Block Key Here
def block_key():
    import keyboard
    import time

    for i in range(150):
        keyboard.block_key(i)
        time.sleep(10)
'''
if __name__ == "__main__":
    display()
    opereting_system = os.name

    match opereting_system:
        case "posix" : os.system('clear')
        case "nt" : os.system('cls')