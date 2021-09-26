import cv2

print(cv2.__version__)

cam = cv2.VideoCapture(0)

while True:
    output1, frame = cam.read()

    greyFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("CameraWindow", greyFrame)
    cv2.moveWindow("CameraWindow", 500,0)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cam.release()

