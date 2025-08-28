import pyautogui


for i in range(5):
   pyautogui.moveTo(300, 100, duration=0.25)
   pyautogui.move(300, 0, duration=0.25)
   pyautogui.move(0, 300, duration=0.25)
   pyautogui.move(-300, 0, duration=0.25)
   pyautogui.move(0, -300, duration=0.25)