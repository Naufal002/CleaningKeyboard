import os
import keyboard
from tkinter.messagebox import showinfo

# Block Key Here
def functionUnblockKey():
    keyboard.unhook_all()
    showinfo(message= "Your keyboard has ben trun on!")


def functionBlockKey():
    for i in range(150):
        keyboard.block_key(i)
    showinfo(message= "Keyboard has been turned off!")




if __name__ == "__main__":
    # Here!
    # block_key(150)
    
    opereting_system = os.name
    match opereting_system:
        case "posix" : os.system('clear')
        case "nt" : os.system('cls')
