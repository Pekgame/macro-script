import keyboard
import win32api, win32con
left_macro = input('Select Button To Left Macro Click> ')
right_macro = input('Select Button To Right Macro Click> ')
print('You can now used the macro!')
def left_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def right_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
while True:
    while keyboard.is_pressed(left_macro) == True:
        left_click()
        left_click()
        left_click()
    while keyboard.is_pressed(right_macro) == True:
        right_click()
        right_click()
        right_click()
