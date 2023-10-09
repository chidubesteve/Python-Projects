import cv2
import time

video = cv2.VideoCapture(0)

timer = int(10)

while True:
    ret,frame = video.read()
    cv2.imshow('Frame', frame)
    k = cv2.waitKey(1)
    if k == ord('t'):
        prev = time.time()
        while timer >= 0:
            ret,frame = video.read()
            cv2.putText(frame, str(timer), (200, 250), cv2.FONT_HERSHEY_COMPLEX, 7, (0,255,0), 4, cv2.LINE_AA)
            cv2.imshow('Frame', frame)
            cv2.waitKey(100)
            cur = time.time()
            if cur - prev > 1:
                prev = cur
                timer -= 1
        else:
            ret,frame = video.read()
            cv2.imshow('Frame', frame)
            cv2.waitKey(1000)
            cv2.imwrite('camera.jpg', frame)
            
            
    elif k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()