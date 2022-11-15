import os
if __name__ == "__main__":
    opereting_system = os.name

    match opereting_system:
        case "posix" : os.system('clear')
        case "nt" : os.system('cls')


import tkinter as tk
from tkinter import ttk

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
    input_frame = ttk.Frame()

    # Label
    Label = ttk.Label(input_frame, text="Disable Your Keyboard: ")
    Dummy_label = ttk.Label(input_frame, text="")


    # Combobox
    data_combobox = ['Disable', 'Undisable']
    Combobox = ttk.Combobox(input_frame, values= data_combobox)

    # Button
    Seccond_Dummy_label = ttk.Label(input_frame, text="")
    Button = ttk.Button(input_frame, text= "Press")

    # Pack
    input_frame.pack(padx=10,pady=10,fill='x',expand=True)
    Label.pack()
    Dummy_label.pack()
    Combobox.pack()
    Seccond_Dummy_label.pack()
    Button.pack()
    MW.mainloop()
    
display()