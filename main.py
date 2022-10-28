# Automating Whatsapp, Facebook, Instagram Chat.


# Importing Required Modules. 

# You can install these modules from your terminal.

# Command for that is 
# (sudo python3 -m pip install pyautogui).(Note: Use cammand without brackets).


import pyautogui
import time


time.sleep(5)
text = "The text you want to send"

# Now writing while loop.

while True:
    pyautogui.typewrite(text)
    time.sleep(1)
    pyautogui.press('enter')


# Now, open the chat messenger in your browser in a new tab. Once done, save and run the python script. Once the execution starts, make sure to place your cursor in the right place (Text box, where you write message).

# In order to stop the program you need to manually stop it in your code editor.

# Good Luck!. 