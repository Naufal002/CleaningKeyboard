import os
if __name__ == "__main__":
    opereting_system = os.name

    match opereting_system:
        case "posix" : os.system('clear')
        case "nt" : os.system('cls')


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Display Here!
def display():
    '''FUNCTION DISPLAY'''
    Main_Window = tk.Tk()

    Main_Window.iconbitmap('C:/Users/Administrator/Documents/CleaningKeyboard/Assets/icon2.ico')
    Main_Window.geometry('300x200')
    Main_Window.title('Cleaning Keyboard')
    Main_Window.configure(bg='white')
    Main_Window.resizable(False,False)

    atribut(Main_Window)

# Atribut Here!
def atribut(MW):
    '''FUNCTION ATRIBUT'''
    from Disable_Keyboard import block_key

    input_frame = ttk.Frame()
    # Label
    Label = ttk.Label(input_frame, text="Disable Your Keyboard: ")
    Seccond_label = ttk.Label(input_frame, text="-Close the program to end process-")

    # Combobox
    # data_combobox = ['Disable', 'Undisable']
    # Combobox = ttk.Combobox(input_frame, values= data_combobox)

    # Button
    Seccond_Dummy_label = ttk.Label(input_frame, text="")
    Button = ttk.Button(input_frame, text= "Disable!", command= block_key)

    # Pack
    input_frame.pack(padx=10,pady=10,fill='x',expand=True)
    Label.pack()
    Seccond_label.pack()
    # Combobox.pack()
    Seccond_Dummy_label.pack()
    Button.pack()
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
display()