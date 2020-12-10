import pyautogui
import time

time.sleep(1)

spam_text = "hello"

for _ in range(50):
    pyautogui.typewrite(spam_text)
    pyautogui.press('enter')
    time.sleep(0.5)
    if spam_text == range:
        time.sleep(0.5)
        break

