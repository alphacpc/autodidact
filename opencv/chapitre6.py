import cv2;
import numpy as np;

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
    img = cv2.imread("assets/dodge.jpeg");
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV);
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
    imgResult = cv2.bitwise_and(img,img, mask=mask)

    allImg = np.hstack((img, imgHSV, imgResult))
    
    cv2.imshow("ALl Image", allImg);
    # cv2.imshow("Image HSV", imgHSV);
    # cv2.imshow("Image Result", imgResult);

    cv2.waitKey(1);
    


cv2.destroyAllWindows();