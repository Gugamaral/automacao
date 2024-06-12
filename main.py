import pyautogui as auto
import time

auto.PAUSE = 0.5

auto.press('win')
auto.write('chrome')
auto.press('enter')

auto.write('github.com')
auto.press('enter')

time.sleep(3)
auto.hotkey('ctrl', 't')
auto.write('classroom.google.com')
auto.press('enter')

auto.hotkey('alt', 'space')
auto.press('x')
