import cv2
import joblib
cap = cv2.VideoCapture(0) #source can be an existing video file or port number of webcam
start = False
count = 0
categories = ['rock', 'paper', 'scissors', 'nothing']
model = joblib.load('rockpaperscissors.pkl')
while cap.isOpened():     #Continue till video feed is being read
    _, frame = cap.read() #Read the video feed frame by frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame, (7,7), 0)
    cv2.rectangle(frame, (150,100), (450,350), (255,0,0), 5)
    _, threshold = cv2.threshold(frame, 160, 255, cv2.THRESH_BINARY)
    roi = threshold[100:350,150:450]
    frame[100:350,150:450] = roi
    # cv2.resize(roi, (64,64))
    roi = cv2.cvtColor(roi,cv2.COLOR_GRAY2BGR)
    roi = roi.flatten()
    roi = roi.reshape(1,-1)
    roi = roi / 255
    prediction = model.predict(roi)
    print(prediction)
    print(categories[prediction[0]])
    cv2.putText(frame, categories[prediction[0]], (0, 50), cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,0), 3)
    cv2.imshow("Video", frame) #show the video feed
    if cv2.waitKey(1) == ord('q'): #if the q key is pressed 
        break
    if cv2.waitKey(33) == ord('s'):
        start = True

cap.release() #Stop the capture
cv2.destroyAllWindows() #Close all windows