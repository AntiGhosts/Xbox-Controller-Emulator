import keyboard  
from XboxController import XboxController

mapping = {
    'a': 'LS_left',
    'w': 'LS_up',
    's': 'LS_down',
    'd': 'LS_right',
    'e': 'X',
    'left_click': 'RT', 
    'right_click': 'RB',
    'space': 'A',
    'q': 'B',
    't': 'Y',
    'r': 'RS', #right stick
    'f': 'LT', #left trigger
    'g': 'RT', #right trigger
    'h': 'LB', #left bumper 
    'j': 'RB'  #right bumper
}

controller = XboxController()

def handle_key_press(key):
    if key in mapping:
        controller.press_button(mapping[key])

keyboard.on_press(handle_key_press)
keyboard.wait()
