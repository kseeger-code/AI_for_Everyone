import cv2

cam = cv2.VideoCapture(0) # Set up camera object

while True:

    trash, frame = cam.read() # get a frame

    greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # create a grey version of frame

    # create top left window
    cv2.imshow("topLeft", frame)
    cv2.moveWindow("topLeft", 0, 0)

    # create top right window
    cv2.imshow("topRight", greyFrame)
    cv2.moveWindow("topRight",500,0)

    # create bottom left window
    cv2.imshow("bottomLeft", greyFrame)
    cv2.moveWindow("bottomLeft", 0, 500)

    # create bottom right window
    cv2.imshow("bottomRight", frame)
    cv2.moveWindow("bottomRight", 500, 500)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break
cam.release()

