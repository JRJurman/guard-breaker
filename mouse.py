import win32api
import sys
from win32api import GetSystemMetrics

displayWidth = 1920 #GetSystemMetrics(0)
displayHeight = 1080 #GetSystemMetrics(1)

#the webcam we used was 640 x 480 

camResHeight = 640
camResWidth = 480

for line in sys.stdin:
    newX, newY = line.split()
    newX = int(newX)
    newY = int(newY)
    
    print(str(int(displayWidth * (newX/camResWidth))) + ' ' + str(int(displayHeight * (newY/camResHeight))))
    sys.stdout.flush()
    #win32api.SetCursorPos((int(newX * (displayWidth/camResWidth)), int(newY * (displayHeight/camResHeight))))
 
