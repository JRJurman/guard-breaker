import numpy as np
import cv2

#Select video input; 0 for default video
cap = cv2.VideoCapture(1)

TOP = 0; RIGHT = 1; BOTTOM = 2; LEFT = 3;
def checkEdge(image, edge, rows, threshold=True):
    """
    checkEdge is a function that takes in an image and an edge to check,
    and returns if there are values in that edge.

    image is the image to check for edges.

    edge is an integer corresponding to the following values:
    TOP = 0; RIGHT = 1; BOTTOM = 2; LEFT = 3;

    rows is an integer that is the number of rows to be checked from the edge.

    If threshold is an integer, then return true or false the
    summed rows are greater than the threshold.

    Otherwise, return an integer that is the value of the summed rows.
    """

    # rotate the image so the top row is the interesting one
    rotImg = np.rot90(image, edge)

    # crop the image so we can do a dumb sum
    cropImg = rotImg[:rows, :]

    edgeSum = np.sum(cropImg)

    if (threshold == True):
        return edgeSum
    return edgeSum > threshold

def findPoint(image, brokenEdge):
    """
    findPoint finds the coordinate opposite from the direction we broke

    image is the image we're scanning

    brokenEdge is the edge we broke with our arm
    """

    # determine the side to approach from,
    # depending on the side we broke
    pointEdge = (brokenEdge + 2) % 4

    # rotate the image so the top row is the interesting one
    rotImg = np.rot90(image, pointEdge)

    # sum across the rows
    sumRows = np.sum(rotImg, axis=1)

    # get the first index where there is a value
    nonZeroRows = np.nonzero(sumRows)[0]
    targetRow = nonZeroRows[0]

    # get the first index of that row from the rotated image
    targetColumn = np.nonzero(rotImg[targetRow])[0][0]

    # depending on the rotation, mutate the coords
    if ((pointEdge % 2) == 1):
        targetRow, targetColumn = targetColumn, targetRow
    if ((pointEdge == 1) or (pointEdge == 2)):
        targetColumn = np.shape(image)[1] - targetColumn
    if ((pointEdge == 2) or (pointEdge == 3)):
        targetRow = np.shape(image)[0] - targetRow

    #print("SHAPE: {0}".format(np.shape(image)))
    #print("POINT EDGE: {0}".format(pointEdge))

    return [targetRow, targetColumn]

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # transform the image read into a grayscale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (10,10))

    # do our edge detection here
    # we do canny in this example, but this SHOULD BE TWEAKED based on your
    # application and real-world settings.
    # http://docs.opencv.org/2.4/modules/imgproc/doc/feature_detection.html
    edges = cv2.Canny(gray, 50, 50)


    # determine what edge we are coming from
    coord = []
    targetEdge = -1
    if ( checkEdge( edges, TOP, 20, 1000 ) ):
        targetEdge = TOP
    elif ( checkEdge( edges, LEFT, 20, 1000 ) ):
        targetEdge = LEFT
    elif ( checkEdge( edges, BOTTOM, 20, 1000 ) ):
        targetEdge = BOTTOM
    elif ( checkEdge( edges, RIGHT, 20, 1000 ) ):
        targetEdge = RIGHT

    # if any edge was broken with some confidence, find a coordinate
    if (targetEdge > -1):
        coord = findPoint( edges, targetEdge )

    # Display the resulting frame
    if (len(coord) > 0):
        gray[coord[0]-10:coord[0]+10, coord[1]-10:coord[1]+10] = 255
        edges[coord[0]-10:coord[0]+10, coord[1]-10:coord[1]+10] = 255
    cv2.imshow('gray', gray)
    cv2.imshow('edges', edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
