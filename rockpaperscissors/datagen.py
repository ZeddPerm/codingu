import cv2
import numpy as np
cap = cv2.VideoCapture(0) #source can be an existing video file or port number of webcam
start = False
count = 0
while cap.isOpened():     #Continue till video feed is being read
    _, frame = cap.read() #Read the video feed frame by frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame, (7,7), 0)
    cv2.rectangle(frame, (150,100), (450,350), (255,0,0), 5)
    roi = frame[100:350,150:450]
    frame[100:350,150:450] = roi
    print(roi)
    cv2.imshow("Video", frame) #show the video feed
    if start:
        if count == 500:
            break
        else:
            count += 1
            print(count)
            cv2.resize(roi, (64,64))
            cv2.imwrite(f'D:/Documents/codingu/rockpaperscissors/images/rock/rock{count}.png', roi)
    if cv2.waitKey(1) == ord('q'): #if the q key is pressed
        break
    if cv2.waitKey(33) == ord('s'):
        start = True

cap.release() #Stop the capture
cv2.destroyAllWindows() #Close all windows
