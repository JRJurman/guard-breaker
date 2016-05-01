import win32api
import sys

for line in sys.stdin:
    newX, newY = line.split()
    win32api.SetCursorPos((int(newX), int(newY)))
 
