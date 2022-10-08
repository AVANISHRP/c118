import cv2
from cv2 import VideoCapture
ing = cv2.imread("walking.avi")

# Create our body classifier
body_classifier = cv2.CascadeClassifier("haarcascade_fullbody.xml")

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    cv2.cvtColor(VideoCapture, cv2.COLOR_BGR2GRAY),
    
    # Read first frame
    ret, frame = cap.read()
    cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),

    #Convert Each Frame into Grayscale
    
    # Pass frame to our body classifier
    
    body_classifier = cv2.CascadeClassifier("haarcascade_fullbody.xml")
    
    
    # Extract bounding boxes for any bodies identified
    

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
