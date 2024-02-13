import pyautogui
from time import sleep

pyautogui.click(302,736, duration=0.5)
pyautogui.sleep(1)
pyautogui.hotkey('win', 'r')
pyautogui.sleep(0.5)
pyautogui.press('enter')

pyautogui.sleep(1)
pyautogui.write('cd projetos')
pyautogui.press('enter')

pyautogui.sleep(0.5)
pyautogui.write('npx create-next-app@latest teste1')
pyautogui.press('enter')

pyautogui.sleep(1)

pyautogui.press('enter')
pyautogui.sleep(1)

pyautogui.press('enter')
pyautogui.sleep(1)

pyautogui.press('enter')
pyautogui.sleep(1)

pyautogui.press('enter')
pyautogui.sleep(1)

pyautogui.press('enter')
pyautogui.sleep(1)

pyautogui.press('enter')

pyautogui.sleep(40)
pyautogui.write('cd teste1')
pyautogui.press('enter')
pyautogui.sleep(1)

pyautogui.write('code .')
pyautogui.sleep(1)

pyautogui.press('enter')
