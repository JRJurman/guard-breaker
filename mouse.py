import win32api
import sys
from win32api import GetSystemMetrics

displayWidth = 1920 #GetSystemMetrics(0)
displayHeight = 1080 #GetSystemMetrics(1)

#the webcam we used was 640 x 480 

camResHeight = 640
camResWidth = 480

print("DH= ", displayHeight)
print("DW= ", displayWidth)
print("CH= ", camResHeight)
print("CW= ", camResWidth)

for line in sys.stdin:
    newY, newX = line.split()
    newX = int(newX)
    newY = int(newY)

    #print(int(newX * (displayWidth/camResWidth)), int(newY * (displayHeight/camResHeight)))
    #sys.stdout.flush()
    win32api.SetCursorPos((int(newX * (displayWidth/camResWidth)), int(newY * (displayHeight/camResHeight))))
 
