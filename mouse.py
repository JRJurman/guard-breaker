import win32api
import sys
import socket

displayWidth = 1920 #GetSystemMetrics(0)
displayHeight = 1080 #GetSystemMetrics(1)

# the webcam we used was 640 x 480 
camResHeight = 640
camResWidth = 480

# Networking Constants
TCP_IP = '129.21.83.117' # IP Address here
TCP_PORT = 9999 # Port Number here
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

for line in sys.stdin:
    newX, newY = line.split()
    newX = int(newX)
    newY = int(newY)
    
    # Construct coordinate string

    coord = str(int(displayWidth * (newX/camResWidth))) + ' ' + str(int(displayHeight * (newY/camResHeight))) + '\n'

    # uncomment to send output to stdout
    print(coord, end='')
    sys.stdout.flush()

    s.send(coord.encode('utf-8'))

s.close()
