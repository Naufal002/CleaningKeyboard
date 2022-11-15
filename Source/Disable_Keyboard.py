import os
if __name__ == "__main__":
    opereting_system = os.name

    match opereting_system:
        case "posix" : os.system('clear')
        case "nt" : os.system('cls')


# Block Key Here
def block_key():
    import keyboard
    import time

    for i in range(150):
        keyboard.block_key(i)
        time.sleep(3600)