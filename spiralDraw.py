# Simple drawing script once MSpaint is open

import pyautogui, time, subprocess

subprocess.Popen('C:\\Windows\\System32\\mspaint.exe')
time.sleep(5)
pyautogui.click()  # Click to make the window active
distance = 300
change = 20
while distance > 0 :
    pyautogui.drag(distance, 0, duration=0.2)  # Move right
    distance -= change
    pyautogui.drag(0, distance, duration=0.2)  # Move down
    pyautogui.drag(-distance, 0, duration=0.2)  # Move left
    distance -= change
    pyautogui.drag(0, -distance, duration=0.2)  # Move up