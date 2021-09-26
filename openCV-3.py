import cv2

width = 640
height = 360


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

while True:

    junk, frame = cam.read()

    cv2.imshow("CameraWindow", frame)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cam.release()

