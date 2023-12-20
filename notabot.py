import subprocess
import pyautogui
import time
from PIL import ImageGrab  # screenshot
import pytesseract
from pytesseract import Output

link = 'https://youtu.be/GVPKVxeXVxA?si=2WJwd0QFGg2U1SYR'
# Linki dırnaq içinde yaz
a = 1 # a-ni bos ver
duration = 16 # video uzunlugu(saniye)
def open_tor():
    # careful about the / when you it's usually \
    subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe"],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
    time.sleep(5)  # to give plenty of time for Tor to load
    pyautogui.hotkey('shift', 'ctrl' , 'n')
    time.sleep(2)


def quit_tor():
    pyautogui.click(x=980, y=30)


def play_playlist():
    pyautogui.click(x=300, y=80)
    pyautogui.typewrite(link)
    pyautogui.press('enter')
    time.sleep(20)  # for loading of video
    pyautogui.press('space')  # start the video


def check_accept(data):
    if 'Before you continue' in data:
        pyautogui.click(x=770, y=890)


def anti_bot(data, reset):
    if 'google.com' in data or reset is True:
        print('hello')


if __name__ == '__main__':
    hard_reset = 0
    open_tor()
    play_playlist()
    while (a != 0):
        time.sleep(duration)
        pyautogui.click(x=94, y=63)
    for increments in range(600):
        hard_reset += 1
        if (hard_reset >= 60):  # reset every hour to simulate many viewers
            anti_bot(data, True)
            hard_reset = 0
