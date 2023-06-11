from pynput import keyboard
from pynput.keyboard import Key, Controller
import string
import random

keyboard_controller = Controller()
def random_string(min_length=5, max_length=10):
    letters = string.ascii_lowercase + "şçöğüı"
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(letters) for i in range(length))

def on_press(key):
    try: k = key.char 
    except: k = key.name 
    if k == 'q':
        random_str = ''.join(random_string() for _ in range(3))
        keyboard_controller.type(random_str)

listener = keyboard.Listener(on_press=on_press)
listener.start()  
listener.join()


Oto Random  Atıcı
