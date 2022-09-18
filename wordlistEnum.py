import urllib.request
import pyautogui, time
import keyboard

time.sleep(0)
word_url = "https://www.mit.edu/~ecprice/wordlist.100000"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()

while keyboard.is_pressed("q") == False:
    for i in words:
        pyautogui.typewrite(i)
        pyautogui.press("enter")
    if keyboard.is_pressed("q") == True:
        break

