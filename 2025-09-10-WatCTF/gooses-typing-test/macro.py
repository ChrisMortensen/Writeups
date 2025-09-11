from pynput.keyboard import Controller
from pynput.mouse import Listener
import time

text_to_type = ""
wpm = 700

# Calculate delay
cmp = wpm * 6 # Assuming average word length of 5 + 1 space
cps = cmp / 60
delay = 1 / cps

keyboard = Controller()

def on_click(x, y, button, pressed):
    if pressed and str(button) == 'Button.left':
        time.sleep(0.5)  # Accounting for site response to click
        for char in text_to_type:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(delay)
        # Stop listener
        return False

# Start listening for clicks
with Listener(on_click=on_click) as listener:
    listener.join()
