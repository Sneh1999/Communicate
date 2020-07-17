import cv2

# This starts a webcam
cap = cv2.VideoCapture(0)
# define width
cap.set(3, 640)
# define height
cap.set(4, 480)
# define brightness
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break