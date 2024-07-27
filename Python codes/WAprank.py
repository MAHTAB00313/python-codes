import  pyautogui
import time
time.sleep(10)
count=0
while count<=10:
   pyautogui.typewrite("In Hanoi question,\nwe can simply transfer all the (n-1) disk to the helper tower and then transfer the last disk to destination and after that we can send rest of the disks from helper tower to destination tower. \nwill this logic work in this question? ")
pyautogui.press("enter")

count = count+1
 

