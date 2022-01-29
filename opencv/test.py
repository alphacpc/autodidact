import cv2;
import numpy as np;

video = cv2.VideoCapture(0)

#Function
def empty(a):
    pass;


# TrackBar
cv2.namedWindow("TrackBars");
# cv2.resize(640,240);
cv2.createTrackbar("Couleur min","TrackBars",0,170,empty);
cv2.createTrackbar("Couleur max","TrackBars",193,255,empty);
cv2.createTrackbar("Sat min","TrackBars",91,255,empty);
cv2.createTrackbar("Sat max","TrackBars",255,255,empty);
cv2.createTrackbar("Val min","TrackBars",43,255,empty);
cv2.createTrackbar("Val max","TrackBars",255,255,empty);

while True:
    success, frame = video.read()
    imgHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV);
    h_min = cv2.getTrackbarPos("Couleur min", "TrackBars");
    h_max = cv2.getTrackbarPos("Couleur max", "TrackBars");
    s_min = cv2.getTrackbarPos("Sat min", "TrackBars");
    s_max = cv2.getTrackbarPos("Sat max", "TrackBars");
    v_min = cv2.getTrackbarPos("Val min", "TrackBars");
    v_max = cv2.getTrackbarPos("Val max", "TrackBars");

    print(h_min, h_max, s_min, s_max, v_min, v_max);
    lower = np.array([h_min, s_min, v_min]);
    upper = np.array([h_max, s_max, v_max]);
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(frame,frame, mask=mask)

    allImg = np.hstack((frame, imgHSV, imgResult))
    
    cv2.imshow("ALl Image", allImg);
    cv2.imshow("Image Mask", mask);
    # cv2.imshow("Image Result", imgResult);

    if cv2.waitKey(1) == ord("q"):
        break
    


cv2.destroyAllWindows();