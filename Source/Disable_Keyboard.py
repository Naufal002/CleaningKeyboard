import os
if __name__ == "__main__":
    opereting_system = os.name

    match opereting_system:
        case "posix" : os.system('clear')
        case "nt" : os.system('cls')

# Block Key Here
def block_key():
    from tkinter.messagebox import showinfo
    import keyboard
    for i in range(150):
        keyboard.block_key(i)
    showinfo(message= "Keyboard has been turned off!")
